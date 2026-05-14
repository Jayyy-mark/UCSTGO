from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class StudentResult(db.Model):
    """Model for Alumni Results"""
    __tablename__ = 'student_results'
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    degree = db.Column(db.String(50))

    def to_dict(self):
        return {
            'roll_no': self.roll_no,
            'name': self.name,
            'year': self.year,
            'gpa': self.gpa,
            'degree': self.degree
        }

class Announcement(db.Model):
    """Model for News and Announcements"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

class Event(db.Model):
    """Model for Tech Fests and Seminars"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    image_url = db.Column(db.String(200))
    description = db.Column(db.Text)