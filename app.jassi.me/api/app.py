from flask import Flask
from routes import minify_css

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

app.register_blueprint(minify_css)

if __name__ == '__main__':
    app.run()
