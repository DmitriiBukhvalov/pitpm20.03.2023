
from flask import Flask, request, current_app
from main import app


with app.test_request_context('/products'):
    request.path  
    request.method
    current_app.name

app = Flask(__name__)

@app.route('/')
def requestdata():
    return "Hello! Your IP is {} and you are using {}: ".format(request.remote_addr,  
                                                                request.user_agent)

if __name__ == "__main__":
    app.run(debug=True)
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT=int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT= 5555
    app.run(HOST, PORT)