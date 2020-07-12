from flaskwebsite import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__ (self):
        return f"City({self.name})"
