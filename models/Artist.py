class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    webpage_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean(),nullable = False, default = False)
    description = db.Column(db.String(500), nullable = True)
    shows = db.relationship('Venue',secondary = Show, backref = db.backref('Artist',lazy = False))
    #add shows (artist has many shows)