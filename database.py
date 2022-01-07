import sqlite3

# Program to create a database
def create_database():
    conn = sqlite3.connect('movie.db')
    c= conn.cursor()
    c.execute("""CREATE TABLE movies(
        name text,
        actor text,
        actress text, 
        director text,
        year_release integer
    )
        """)
    conn.commit()
    conn.close()

# Program to insert values in a database
def insert_database(many_movies):
    conn = sqlite3.connect('movie.db')
    c= conn.cursor()
    c.executemany("INSERT into movies VALUES(?,?,?,?,?)",(many_movies))
    conn.commit()
    conn.close()


# Program to select all records in a database
def select_all():
    conn = sqlite3.connect('movie.db')
    c= conn.cursor()
    print('---- Database Records with all records ----')
    c.execute('SELECT rowid, * FROM movies')
    records=c.fetchall();
    for record in records:
        print(record)
    conn.commit()
    conn.close()

# Program to select a record with a actor name in a database
def select_actor(actor_name):
    conn = sqlite3.connect('movie.db')
    c= conn.cursor()
    print('---- Database Records with actor:',actor_name,' ----')
    c.execute('SELECT * FROM movies WHERE actor = (?)',(actor_name,))
    records=c.fetchall();
    for record in records:
        print(f'Name: {record[0]}, Actor: {record[1]}, Actress: {record[2]}, Director: {record[3]}, Release Date: {record[4]}')
    conn.commit()
    conn.close()