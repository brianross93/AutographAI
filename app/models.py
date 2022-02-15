# Create the models here.

# Create the database model for a user to save essay in. 
# This model should shave a user, the prompt/thesis they entered, and the generated essay.

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Create the database model for a user to save essay in.
# This model should shave a user, the prompt/thesis they entered, and the generated essay.
class UserEssay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', back_populates='essay', uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    prompt = db.Column(db.String(2000))
    generated_essay = db.Column(db.String(200000))

    def __repr__(self):
        return f"UserEssay('{self.user_id}', '{self.prompt}', '{self.generated_essay}')"
#Create the user model. This user model will have a user id that is referenced in the UserEssay model.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(200))
    essay = db.relationship('UserEssay', back_populates='user')

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"
    
# Create the database relationship table between UserEssay and User. 
# This will allow us to have a one to many relationship between the two models.
class UserEssayRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_essay = db.Column(db.Integer, db.ForeignKey('user_essay.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"UserEssayRelationship('{self.user_essay}', '{self.user}')"


