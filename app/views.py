from flask import Blueprint, jsonify, request
from flasgger import swag_from
from .models import User, Repository
from .extensions import db
import requests
from flask import render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/api/user/<username>', methods=['GET'])
def get_user_data(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            "username": user.username,
            "avatar_url": user.avatar_url,
            "public_repos": user.public_repos,
            "followers": user.followers,
            "repositories": [
                {
                    "name": repo.name,
                    "stars": repo.stars,
                    "forks": repo.forks,
                    "language": repo.language,
                    "url": repo.url,
                    "description": repo.description
                } for repo in user.repositories
            ]
        })

    resp = requests.get(f"https://api.github.com/users/{username}")
    if resp.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    data = resp.json()
    user = User(
        username=data["login"],
        avatar_url=data["avatar_url"],
        public_repos=data["public_repos"],
        followers=data["followers"]
    )
    db.session.add(user)
    db.session.commit()

    repos = requests.get(data["repos_url"]).json()
    for r in repos:
        repo = Repository(
            name=r["name"],
            stars=r["stargazers_count"],
            forks=r["forks_count"],
            language=r["language"],
            url=r["html_url"],
            description=r["description"],
            user=user
        )
        db.session.add(repo)
    db.session.commit()

    return jsonify({
        "username": user.username,
        "avatar_url": user.avatar_url,
        "public_repos": user.public_repos,
        "followers": user.followers,
        "repositories": [
            {
                "name": repo.name,
                "stars": repo.stars,
                "forks": repo.forks,
                "language": repo.language,
                "url": repo.url,
                "description": repo.description
            } for repo in user.repositories
        ]
    })

@main.route('/api/repo/<username>/<repo_name>/readme', methods=['GET'])
@swag_from({
    'tags': ['Repository'],
    'description': 'Get README for a repository',
    'parameters': [
        {
            'name': 'username',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The GitHub username'
        },
        {
            'name': 'repo_name',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The repository name'
        }
    ],
    'responses': {
        '200': {
            'description': 'Successful response',
            'schema': {
                'type': 'object',
                'properties': {
                    'readme': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'README not found'
        }
    }
})
def get_repository_readme(username, repo_name): 
    from .github_api import get_repo_readme
    readme_content = get_repo_readme(username, repo_name)
    
    if readme_content:
        repo = Repository.query.filter_by(
            user_id=User.query.filter_by(username=username).first().id,
            name=repo_name
        ).first()
        if repo:
            repo.readme = readme_content
            db.session.commit()
        
        return jsonify({"readme": readme_content})
    
    return jsonify({"readme": None})
