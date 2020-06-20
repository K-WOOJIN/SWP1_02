from cgi import parse_qs
from template import html

def isInt(num) :
    try :
	tmp = int(num)
	return True
    except ValueError :
	return False


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    x = d.get('x', [''])[0]
    y = d.get('y', [''])[0]
    sum, mult = "No INPUT", "No INPUT"
    if isInt(x) and isInt(y) :
	x, y = int(x), int(y)
	sum, mult = x + y, x * y
    response_body = html % {
	'sum':sum,
	'mult':mult
	}
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
