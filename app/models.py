from . import db

class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date
        }
