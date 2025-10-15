from bottle import route, run, template, view, static_file

@route('/')
@view('home')
def home():
    return {}

@route('/climate')
@view('climate')
def climate():
    return {}

@route('/about')
@view('about')
def home():
    return {}

@route('/solution')
@view('solution')
def solution():
    return {}

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)