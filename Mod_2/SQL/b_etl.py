import requests
import json
import config
import mysql.connector

cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.pw,
    database = 'yelp_tea'

)

cursor = cnx.cursor()

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
            "radius" : radius,
            "limit": limit

             }

def yelp_call(url_params, headers, url):
    print(headers)
    response = requests.get(url, headers=headers, params=url_params)
    data = response.json()
    return data['businesses']

def parse_data(businesses):
    parsed_data = []
    for business in businesses:
        if 'price' in business.keys():
            biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], business['price'])
            parsed_data.append(biz_tuple)
        else:
            biz_tuple = (business['id'], business['name'], None, business['rating'], business['review_count'])
            parsed_data.append(biz_tuple)
    return parsed_data

def db_insert(cnx, cursor, parsed_results):
    add_business = ("""INSERT INTO yelp_businesses
               (business_id, name, rating, review_count, price)
               VALUES (%s, %s, %s, %s, %s)""")
    cursor.executemany(add_business, parsed_results)
    cnx.commit()

def paginate(url_params, headers, url, max=266):
    cur = 0
    while cur < max:
        url_params['offset'] = cur
        businesses = yelp_call(url_params, headers, url)
        parsed_results = parse_data(businesses)
        db_insert(cnx, cursor, parsed_results)
        cur += 50

#cnx = mysql.connector .connect(
#    host = config.host,
#    user = config.user,
#    passwd = config.pw
#)

paginate(url_params, headers, url)
