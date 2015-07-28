import requests, json

URBANDICT_TERM_URL = "http://api.urbandictionary.com/v0/define?term="
term = ''

# commands
def show_related_terms():
    response = get_term()
    tags = ''
    for tag in response['tags']:
        tags = tags + (', ' if tags != '' else '') + tag
    print('tags')
    print(tags)

def show_term(size):
    response = get_term()
    count = 1
    for definition in response['list'][:size]:
        print('')
        print(str(count) + ')')
        print('Definition:')
        print(definition['definition'])
        print('')
        print('Example:')
        print(definition['example'])
        count += 1

# helpers
def get_term():
    global term
    if term == '':
        term = raw_input('search term: ')
    try:
        return requests.get(URBANDICT_TERM_URL + term).json()
    except requests.HTTPError as httpe:
        print('cannot retrieve term')
        print('error response' + httpe.response)

# execute
show_related_terms()
show_term(5)
