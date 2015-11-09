from bottle import route, run

@route('/')
def index():
    return 'Hello, World'

@route('/hello/<name>')
def sayHello(name):
    return 'Hello, ' + name

run(host='0.0.0.0', port=8080)
