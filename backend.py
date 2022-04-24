# backend
import sqlite3


def MovieData():
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID text,Movie_Name text,Release_Date text,Director text,Cast text,Budget text,Duration text,Rating text")
    con.commit()
    con.close()


def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", (Movie_ID,
                Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()


def ViewMovieData():
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows


def DeleteMovieRec(id=""):
    print(id)
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE Movie_ID=?", (id,))
    con.commit()
    con.close()
    print("deleted")


def SearchMovieData(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE Movie_ID=?",
                (Movie_ID,))
    rows = cur.fetchall()
    con.close()
    return rows


def UpdateMovieData(id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",
                (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()
