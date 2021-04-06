# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# con = psycopg2.connect("user=admin password='admin'");
# con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

# cursor          = con.cursor();

# name_Database   = "AudioFilesDB";

# sqlCreateDatabase = "create database "+name_Database+";"

# cursor.execute(sqlCreateDatabase);

from __future__ import print_function

hostname = 'localhost'
username = 'postgres'
password = 'password1234'
database = 'AudioFiles'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )


print( "Using psycopg2:" )
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()

print( "Using PyGreSQL (pgdb):" )
import pgdb
myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
doQuery( myConnection )
myConnection.close()