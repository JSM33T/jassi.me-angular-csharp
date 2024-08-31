# from flask import Blueprint, request
# from csscompressor import compress

# minify_css = Blueprint('minify_css', __name__)

# @minify_css.route('/minify-css', methods=['POST'])
# def minify_css_route():
#     if 'css_text' in request.form:
#         css_text = request.form['css_text']
#         minified_css = compress(css_text)
#         return minified_css
#     else:
#         return 'Please provide CSS text to minify.', 400
from flask import Blueprint, request, send_file
from tempfile import NamedTemporaryFile
from csscompressor import compress

minify_css = Blueprint('minify_css', __name__)

@minify_css.route('/minify-css', methods=['POST'])
def minify_css_route():
    css_text = request.form.get('css_text', None)
    css_file = request.files.get('css_file', None)

    if css_text:
        # Perform CSS minification on the provided text
        minified_css = compress(css_text)
        return minified_css

    elif css_file:
        # Handle CSS file upload for minification
        css_text = css_file.read().decode('utf-8')  # Read file content correctly
        minified_css = compress(css_text)

        # Create a temporary file to store the minified CSS
        temp_file = NamedTemporaryFile(delete=False, suffix='.css')
        temp_file.write(minified_css.encode('utf-8'))
        temp_file.close()

        # Return the minified CSS file as a response
        return send_file(temp_file.name, as_attachment=True, download_name='minified_css.css')

    return 'Please provide CSS text to minify.', 400
