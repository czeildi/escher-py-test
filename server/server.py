from flask import Flask
app = Flask(__name__)

@app.route("/validate_request_js_py")
def validate_js_py():
    return 'Got request on validate_request_js_py'

@app.route("/validate_request_py_py")
def validate_py_py():
    return 'Got request on validate_request_py_py'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9292)
