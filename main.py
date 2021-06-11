from flask import Flask
main=Flask(__name__)
@main.route('/')
def hello():
    return "hello world"


main.run(debug=False,host='0.0.0.0')