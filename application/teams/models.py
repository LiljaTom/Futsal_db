from application import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(144), nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    players = db.relationship("Player", backref = 'team', lazy = True)


    def __init__(self, name):
        self.name = name