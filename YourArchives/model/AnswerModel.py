from YourArchives import db

class Answer(db.Model):
    __tablename__ = 'app_answers'

    id = db.Column(db.Integer(), primary_key=True, name="answer_id")
    user_id = db.Column(db.Integer(), db.ForeignKey('app_users.user_id'))
    question_id = db.Column(db.Integer(), db.ForeignKey('app_questions.question_id'))
    answer_text = db.Column(db.String(length=1024), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime())
    is_active = db.Column(db.Integer())