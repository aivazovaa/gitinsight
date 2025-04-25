from .extensions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_url = db.Column(db.String(256))
    public_repos = db.Column(db.Integer)
    followers = db.Column(db.Integer)

    repositories = db.relationship('Repository', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Repository(db.Model):
    __tablename__ = 'repositories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    stars = db.Column(db.Integer)
    forks = db.Column(db.Integer)
    language = db.Column(db.String(64))
    url = db.Column(db.String(256))
    description = db.Column(db.Text)
    readme = db.Column(db.Text)    

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Repository {self.name}>"
