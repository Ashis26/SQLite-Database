import database

#Creating the database
database.create_database()

#Inserting values in a database
many_movies=[
    ('Pirates of the Caribbean: The Curse of the Black Pearl','Johnny Depp','Keira Knightley','Gore Verbinski',2003),
    ('Pirates of the Caribbean: Dead Man\'s Chest','Johnny Depp','Keira Knightley','Gore Verbinski',2006),
    ('City of Lies','Johnny Depp','Wynn Everett','Brad Furman',2018),
    ('Harry Potter and the Philosopher\'s Stone','Daniel Radcliffe','Emma Watson','Susie Figgis',2001),
    ('Harry Potter and the Goblet of Fire','Daniel Radcliffe','Emma Watson','Mike Newell',2005),
    ('Guns Akimbo','Daniel Radcliffe','Samara Weaving','Jason Lei Howden',2019),
    ('The Hobbit: An Unexpected Journey','Richard Armitage','Cate Blanchett','Peter Jackson',2012),
    ('The Lodge','Richard Armitage','Riley Keough','Veronika Franz',2019),
    ('Phir Hera Pheri','Akshay Kumar','Bipasha Basu','Neeraj Vora',2006),
    ('Kesari','Akshay Kumar','Parineeti Chopra','Anurag Singh',2019)
]
database.insert_database(many_movies)
