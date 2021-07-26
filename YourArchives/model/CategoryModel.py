from YourArchives import db

class Category(db.Model):
    __tablename__ = 'app_categories'

    id = db.Column(db.Integer(), primary_key=True, name="category_id")
    category_name = db.Column(db.String(length=50), nullable=False)
    description = db.Column(db.String(length=255), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime())
    is_active = db.Column(db.Integer(), default=0)