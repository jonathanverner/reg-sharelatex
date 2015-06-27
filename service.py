#!/usr/bin/env python3
from bottle import route, error, run, template, request, response, abort
import simplepam, getent, os, sys

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

if __name__ == "__main__":
    open('reg-service.pid','w').write(str(os.getpid()))

    if len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        address = "localhost"
        port=3023
    run(host=address, port=port, umask=0, reloader=False)

    os.remove('reg-service.pid')