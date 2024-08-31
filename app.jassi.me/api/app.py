from flask import Flask
from routes.css.minify_css import minify_css
from routes.css.format_css import format_css

app = Flask(__name__)

app.register_blueprint(minify_css)
app.register_blueprint(format_css)

if __name__ == '__main__':
    app.run()
