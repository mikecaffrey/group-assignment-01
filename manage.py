from flask_script import Manager
from project import app, db, Movie

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    movie1 = Movie(id = '1', title= 'Just Go With It', actor = 'Adam Sandler', year = "2011", genre = "Comedy", description='On a weekend trip to Hawaii, a plastic surgeon convinces his loyal assistant to pose as his soon-to-be-divorced wife in order to cover up a careless lie he told to his much-younger girlfriend.')
    movie2 = Movie(id = '2', title= 'Maleficent', actor = 'Angelina Jolie', year = '2014', genre ='Fantasy' ,description='A vengeful fairy is driven to curse an infant princess, only to discover that the child may be the one person who can restore peace to their troubled land.')
    movie3 = Movie(id = '3', title= 'Mr. & Mrs. Smith', actor = 'Angelina Jolie', year = '2005', genre='Action', description='A bored married couple is surprised to learn that they are both assassins hired by competing agencies to kill each other.')
    movie4 = Movie(id = '4', title= 'Grown UPs', actor = 'Adam Sandler', year = '2010', genre= 'Comedy', description='After their high school basketball coach passes away, five good friends and former teammates reunite for a Fourth of July holiday weekend.')
    movie5 = Movie(id = '5', title= 'Titantic', actor = 'Leonardo DiCaprio', year = '1997',genre = 'Romance', description='A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.')

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.add(movie5)

    db.session.commit()


if __name__ == "__main__":
    manager.run()
