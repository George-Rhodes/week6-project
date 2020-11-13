from application import db


class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rTitle = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable = False)
    description = db.Column(db.String(255), nullable=False)  
    routine = db.relationship('Excer', backref='routine', cascade="all, delete")

    


class Excer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable=False, ondelete="CASCADE")
    set_name = db.Column(db.String(50), nullable=False)
    level_num = db.Column(db.Integer, nullable = False)
    level_type = db.Column(db.String(10), nullable = False)
    set_length = db.Column(db.Integer, nullable = False)
    set_type = db.Column(db.String(10), nullable = False)
