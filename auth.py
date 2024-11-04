from functools import wraps

from flask import Flask, request, make_response

def execute_auth(original_func):

  @wraps(original_func)
  def decorated(*args, **kwargs):
    auth_header = request.authorization
    if auth_header and auth_header.username == 'DEI' and auth_header.password == 'DEI':
      return original_func(*args, **kwargs)
    return make_response('<h1>Forbidden</h1>', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

  return decorated
