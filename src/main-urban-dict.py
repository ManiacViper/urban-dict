import prof
import requests, json

URBANDICT_TERM_URL = "http://api.urbandictionary.com/v0/define?term="
term = ''

# commands
def show_related_terms(term):
    response = get_term(term)
    tags = ''
    for tag in response['tags']:
        tags = tags + (', ' if tags != '' else '') + tag
    prof.cons_show('tags')
    prof.cons_show(tags)

def show_term(size, term):
    response = get_term(term)
    count = 1
    for definition in response['list'][:size]:
        prof.cons_show('')
        prof.cons_show(str(count) + ')')
        prof.cons_show('Definition:')
        prof.cons_show(definition['definition'])
        prof.cons_show('')
        prof.cons_show('Example:')
        prof.cons_show(definition['example'])
        count += 1

# helpers
def get_term(term):
    try:
        return requests.get(URBANDICT_TERM_URL + term).json()
    except requests.HTTPError as httpe:
        prof.cons_show('cannot retrieve term')
        prof.cons_show('error response' + httpe.response)

def check_term(term):
     if not term:
        prof.cons_bad_cmd_usage("/urban")

def execute(term) :
    check_term(term)
    show_related_terms(term)
    show_term(2, term)

def prof_init(version, status):
    synopsis = [
        "/urban [word]"
    ]
    description = "Display definitions of a slang word"
    args = [
        [ "[word]", "Any slang word you want to find a definition for" ]
    ]
    examples = []

    prof.register_command("/urban", 1, 1, synopsis, description, args, examples, execute)
    prof.completer_add("/urban", [ "[slang word here]" ])
