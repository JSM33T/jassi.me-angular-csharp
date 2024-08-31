from flask import Blueprint, request
from csscompressor import compress

minify_css = Blueprint('minify_css', __name__)

@minify_css.route('/minify-css', methods=['POST'])
def minify_css_route():
    if 'css_text' in request.form:
        css_text = request.form['css_text']
        minified_css = compress(css_text)
        return minified_css
    else:
        return 'Please provide CSS text to minify.', 400
