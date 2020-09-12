from application import db

class Player(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(144), nullable = False)
    number = db.Column(db.Integer, nullable = False)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable = False)

    def __init__(self, name, number):
        self.name = name
        self.number = number
