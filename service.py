from bottle import route, error, run, template, request, response, abort
import simplepam, getent

@route('/user/<name>/authenticate', method='POST')
def authenticate(name):
    data = request.json
    if not data:
        abort(401, "Unable to authenticate: no password given.")
    elif simplepam.authenticate(name, request.json['password']):
        return None
    abort(401, "Unable to authenticate.")

@route('/user/<name>', method='GET')
def user_info(name):
    user = getent.passwd(name);
    if user:
        return dict(user)
    abort(404, "User not found.");

@error(404)
def error404(error):
    return ""

@error(401)
def error404(error):
    return ""


run(host='localhost', port=3023)