from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robot", email="tinnyTim@udacity.com",
             picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()

# Items in Eletronnics
category1 = Category(name="Electronics")

session.add(category1)
session.commit()

item2 = Item(user_id=1, name="Computer",
             description='''A computer is an electronic device that manipulates information, or data.''',
             category=category1)

session.add(item2)
session.commit()


item1 = Item(user_id=1, name="Mobiles",
             description='''An electronic telecommunications device, often referred to as a cellular phone or cellphone.''',
             category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Tablet",
             description='''A tablet is a wireless, portable personal computer with a touchscreen interface.''',
             category=category1)

session.add(item2)
session.commit()


# Items for Clothes
category2 = Category(name="Kitchen")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Crockery Set",
             description='''Plates, dishes, cups, and other similar items, especially ones made of earthenware or china.''',
             category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Knife",
             description='''An instrument composed of a blade fixed into a handle, used for cutting or as a weapon.''',
             category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Spatula",
             description='''An implement with a broad, flat, blunt blade, used for mixing and spreading things, especially in cooking and painting.''',
             category=category2)


# Menu for Panda Garden
category3 = Category(name="Toys")

session.add(category3)
session.commit()


item1 = Item(user_id=1, name="Teddy Bear", description="A soft toy bear.",
             category=category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Scrabble",
             description='''a game in which players build up words on a board from small lettered squares or tiles.''',
             category=category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Chess",
             description='''Chess is a two-player strategy board game played on a chessboard, a checkered gameboard with 64 squares arranged in an 8 by 8 grid. The game is played by millions of people worldwide.''',
             category=category3)

session.add(item3)
session.commit()


# Items for Furniture
category1 = Category(name="Furniture")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Couch",
             description='''A long upholstered piece of furniture for several people to sit on.''',
             category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Dining Table",
             description='''A table on which meals are served in a dining room.''',
             category=category1)

session.add(item2)
session.commit()


print "added menu items!"
