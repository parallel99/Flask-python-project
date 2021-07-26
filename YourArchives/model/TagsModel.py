from YourArchives import db

class Tag(db.Model):
    __tablename__ = 'app_tags'

    id = db.Column(db.Integer(), primary_key=True, name="tag_id")
    tag_name = db.Column(db.String(), nullable=False)
    question_id = db.Column(db.Integer(), db.ForeignKey('app_questions.question_id'))