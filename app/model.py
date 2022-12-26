from datetime import datetime
from database.database import db

class URLShortner(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    original_url = db.Column(db.String(512),unique=True)
    created_at = db.Column(db.DateTime,nullable=False,
        default=datetime.utcnow)
    expired_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)
    
    def __init__(self, original_url):
        self.original_url = original_url
        # self.created_at = created_at
        # self.expired_at = expired_at
        # self.user_id = user_id

    def __repr__(self):
        return '<URL %r>' % self.original_url