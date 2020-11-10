from application import db


class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rTitle = db.Column(db.String(30), nullable=False)
    creator = db.Column(db.String(30), nullable = False)
    descrption = db.Column(db.String(30), nullable=False)
    date_done = db.Column(db.DateTime, nullable=False)    
    routine = db.relationship('Excer', backref='routine')

    


class Excer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable=False)
    set_name = db.Column(db.String(50), nullable=False)
    level_num = db.Column(db.Integer), nullable = False)
    level_type = db.Column(db.String(10), nullable = False)
    set_length = db.Column(db.Interger(), nullable = False)
    set_Type = db.Column(db.String(10), nullable = False)
