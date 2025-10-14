from flask import Flask
app = Flask(__name__)

API_KEY = 'snyk-12345678-90ab-cdef-1234-567890abcdef'

@app.route('/')
def home():
    return 'Bonjour, Caplogy !'

if __name__ == '__main__':

    app.run(debug=True)