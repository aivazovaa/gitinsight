import requests
import markdown
import bleach
from bs4 import BeautifulSoup

GITHUB_API_URL = "https://api.github.com"

def get_user_profile(username):
    url = f"{GITHUB_API_URL}/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"[404] User '{username}' not found.")
    elif response.status_code == 403:
        print("[403] Rate limit exceeded. Try again later.")
    else:
        print(f"[{response.status_code}] Unexpected error for user profile: {response.text}")

    return None
    
def get_repo_readme(owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/readme"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content = response.json().get("content", "")
        import base64
        try:
            markdown_content = base64.b64decode(content).decode("utf-8")
            html_content = markdown.markdown(markdown_content)
            soup = BeautifulSoup(html_content, 'html.parser')
            return str(soup)
        except Exception as e:
            print(f"Error processing README: {e}")
            return None
            
def get_repo_readme(owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/readme"
    headers = {"Accept": "application/vnd.github.v3.html"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        html_content = response.text
 
        allowed_tags = bleach.sanitizer.ALLOWED_TAGS + [
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'p', 'br', 'pre', 'code', 'img', 'a',
            'ul', 'ol', 'li', 'strong', 'em', 'hr'
        ]
        clean_html = bleach.clean(
            html_content,
            tags=allowed_tags,
            attributes={'a': ['href', 'title'], 'img': ['src', 'alt']}
        )
        return clean_html
 
    headers["Accept"] = "application/vnd.github.v3.raw"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        markdown_content = response.text
        html_content = markdown.markdown(markdown_content)
        clean_html = bleach.clean(
            html_content,
            tags=allowed_tags,
            attributes={'a': ['href', 'title'], 'img': ['src', 'alt']}
        )
        return clean_html
    
    return None

def get_user_repos(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    params = {"per_page": 100, "sort": "updated"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"[404] Repositories for '{username}' not found.")
    elif response.status_code == 403:
        print("[403] Rate limit exceeded. Try again later.")
    else:
        print(f"[{response.status_code}] Unexpected error for repos: {response.text}")

    return []

def get_repo_languages(owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/languages"
    response = requests.get(url)

    if response.status_code == 200:
        return list(response.json().keys())
    elif response.status_code == 404:
        print(f"[404] Languages for repo '{owner}/{repo_name}' not found.")
    elif response.status_code == 403:
        print("[403] Rate limit exceeded. Try again later.")
    else:
        print(f"[{response.status_code}] Unexpected error for languages: {response.text}")

    return []
