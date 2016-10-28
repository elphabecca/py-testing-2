from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # Write a function that creates a game
    # and adds it to the database.
    
    monopoly = Game(name='Monopoly', description='Become a ruthless business-person!')
    pictionary = Game(name='Pictionary', description='Have people guess your bad drawings!')
    taboo = Game(name='Taboo', description='Try to describe a given word to a group of your friends in a limited way!')
    anomia = Game(name='Anomia', description='Try not to blank out on the names of some really obvious categories!')
    castles_of_burgundy = Game(name='Castles of Burgundy', description='Get the most victory points by completing the grounds of your castle!')

    db.session.add_all([monopoly, pictionary, taboo, anomia, castles_of_burgundy])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 