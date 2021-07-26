from YourArchives import db

class Question(db.Model):
    __tablename__ = 'app_questions'

    id = db.Column(db.Integer(), primary_key=True, name="question_id")
    user_id = db.Column(db.Integer(), db.ForeignKey('app_users.user_id'))
    question = db.Column(db.String(length=255), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime())
    description = db.Column(db.String(length=1024), nullable=False)
    is_active = db.Column(db.Integer())
    answers = db.relationship('Answer', lazy=True)
    tags = db.relationship('Tag', lazy=True)
    categories = db.relationship('Category', secondary='app_question_categories')