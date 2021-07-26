from YourArchives import db
from datetime import datetime

class QuestionCategories(db.Model):
    __tablename__ = 'app_question_categories'

    id = db.Column(db.Integer(), primary_key=True)
    question_id = db.Column(db.Integer(), db.ForeignKey('app_questions.question_id'))
    category_id = db.Column(db.Integer(), db.ForeignKey('app_categories.category_id'))
    added_at = db.Column(db.DateTime(), default=datetime.now())