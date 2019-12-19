import requests
import json
import config
import mysql.connector

url = 'https://api.yelp.com/v3/businesses/search'

client_id = 'U1F8RNabNLQ1xoiZ4aU0eA'
api_key = 'MWsKI2UOfPh3dk-fo9clIPR1qpgWtoMYqJ9ASIpzS4A0USmzJ3SuFwKeSHBGviPWf_hFBj940yamvqe4ssszQO59x2kh--IWRu5CeUeoSRBnjYuuDCs-bdk42GPpXXYx'

headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

term = "Tea"

location = "Alphabet City"

radius = 1000

limit = 50

url_params = {
            "term": term.replace(' ', '+'),
            "location": location.replace(' ', '+'),
            "radius" : 1000,
            "limit": 50
        }

response = requests.get(url, headers=headers, params=url_params)

data = response.json()

#biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], business['price'] )

def parse_data(businesses):

    parsed_data = []


    for business in businesses:
        if 'price' in business.keys():
            biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], business['price'])
            parsed_data.append(biz_tuple)
        else:
            biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], None)
            parsed_data.append(biz_tuple)
    return parsed_data

business_data = parse_data(data['businesses'])

cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.pw
)

cursor = cnx.cursor()

def create_database(cursor, database):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


create_database(cursor, 'yelp_tea')
#create_database(cursor, 'yelp_tea_review')
