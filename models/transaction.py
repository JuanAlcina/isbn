from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    destination = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(100), nullable=False)