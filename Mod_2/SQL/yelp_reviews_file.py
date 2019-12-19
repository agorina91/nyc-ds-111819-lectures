import requests
import json

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
                "limit" = 50
            }

response = requests.get(url, headers=headers, params=url_params)

data = response.json()

biz_tuple = (business['id'], business['name'], business['rating'], business['review_count'], business['price'] )

def parse_data(businesses):

    parsed_data = []


    for business in businesses:
        if 'price' in business.keys():
            biz_tuple = (business['id'], business['name'], business['price'], business['rating'], business['review_count'])
            parsed_data.append(biz_tuple)
        else:
            biz_tuple = (business['id'], business['name'], None, business['rating'], business['review_count'])
            parsed_data.append(biz_tuple)
    return parsed_data
