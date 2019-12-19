import requests
import json
import config
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'yelp_tea'

cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.pw,
    database = DB_NAME,
    use_pure = True
)

cursor = cnx.cursor()

TABLES = {}
TABLES['yelp_businesses'] = ("""
     CREATE TABLE yelp_businesses (
      business_id varchar(22) NOT NULL,
      name varchar(50) NOT NULL,
      price varchar(4),
      rating decimal(3,2),
      review_count int(22)
      PRIMARY KEY (business_id)
    ) ENGINE=InnoDB""")

TABLES['yelp_reviews'] = ("""
     CREATE TABLE yelp_reviews (
     review_id varchar(22) NOT NULL,
     business_id varchar(22) NOT NULL,
     time_created varchar(20),
     reviews text(1000),
     FOREIGN KEY (business_id) REFERENCES yelp_businesses(business_id),
     PRIMARY KEY (review_id)
    ) ENGINE=InnoDB""")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
