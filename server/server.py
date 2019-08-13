from flask import Flask, request

app = Flask(__name__)

@app.route("/validate_request_js_py")
def validate_js_py():
    print(request.headers)
    return app.make_response(('Got request on validate_request_js_py', 200, dict(request.headers)))

@app.route("/validate_request_py_py")
def validate_py_py():
    print(request.headers)
    return app.make_response(('Got request on validate_request_py_py', 200, dict(request.headers)))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9292)
