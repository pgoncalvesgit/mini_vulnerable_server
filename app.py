from flask import Flask, request, render_template

from auth import execute_auth

app = Flask(__name__, static_folder='static_html')

xss_stored_value_test_1 = "no reflection"
xss_stored_value_test_2 = "no reflection"

MAX_NUMBER_OF_CHARS = 1024 * 1024 * 1024

def render_my_template(filename, reflection):
  if type(filename) != str:
    Exception("NOT STRING")
  with open(filename, "r") as fp:
    content = fp.read()
    return content.replace("**reflection**", reflection)
  return ""


@app.route('/')
@execute_auth
def get_index_page():
  return app.send_static_file('index.html')

@app.route('/xsstest1')
@execute_auth
def xss_test_1():
  reflection = request.args.get('xssInput') 
  if reflection == None or reflection.strip() == "":
    return app.send_static_file('xssExample1.html')
  else:
    return render_my_template('templates/xssReflection.html', reflection)

@app.route('/xsstest2')
@execute_auth
def xss_test_2():
  reflection = request.args.get('xssInput') 
  if reflection == None or reflection.strip() == "":
    return app.send_static_file('xssExample2.html')
  else:
    return render_template('xssReflection.html', reflection=reflection)

@app.route('/xsstest3', methods=['GET'])
@execute_auth
def get_xss_test_3():
  return app.send_static_file('xssExample3.html')

@app.route('/xsstest3', methods=['POST'])
@execute_auth
def xss_test_3():
  reflection = request.form.get('xssInput')
  if reflection == None or reflection.strip() == "":
    return app.send_static_file('xssExample3.html')
  else:
    return render_my_template('templates/xssReflection.html', reflection)

@app.route('/xsstest4')
@execute_auth
def xss_test_4():
  global xss_stored_value_test_1
  
  reflection = request.args.get('xssInput')
  if reflection == None or reflection.strip() == "":
    return app.send_static_file('xssExample4.html')
  else:
    xss_stored_value_test_1 = reflection
    return app.send_static_file('xssExample4.html')


@app.route('/xsstest5')
@execute_auth
def xss_test_5():
  global xss_stored_value_test_2
  
  reflection = request.args.get('xssInput')
  if reflection == None or reflection.strip() == "":
    return app.send_static_file('xssExample5.html')
  else:
    xss_stored_value_test_2 += "<li>" + reflection + "</li>"
    length_of_reflection = len(xss_stored_value_test_2)
    if length_of_reflection > MAX_NUMBER_OF_CHARS:
      xss_stored_value_test_2 = xss_stored_value_test_2[-MAX_NUMBER_OF_CHARS:]
    return app.send_static_file('xssExample5.html')

@app.route('/xxsstored1')
@execute_auth
def xss_stored_1():
  return render_my_template('templates/xssReflection.html', xss_stored_value_test_1)

@app.route('/xxsstored2')
@execute_auth
def xss_stored_2():
  return render_my_template('templates/xssReflectionList.html', xss_stored_value_test_2)


if __name__ == "__main__":
  app.run(debug=True)

