import requests
from settings import keys, testing

POSITION_URL = testing['base_url'] + ':' + testing['port'] + '/' + 'elections/position'


def get_position(position=None, election_type=None, active=None):
    optional_parameters = {
        'position': position,
        'election_type': election_type,
        'active': active
    }
    resp = requests.get(POSITION_URL, optional_parameters)
    return resp


def post_position(position, election_type, active, order):
    post_data = {
      'position': position,
      'election_type': election_type,
      'active': active == 'True',
      'order': int(order)
    }
    resp = requests.post(POSITION_URL, json=post_data)
    return resp

# (r"/elections/position/(.*)", elections.SpecifiedPositionHandler)
# get, put
