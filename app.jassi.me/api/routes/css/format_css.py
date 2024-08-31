# from flask import Blueprint, request
# import cssbeautifier

# format_css = Blueprint('format_css', __name__)

# @format_css.route('/format-css', methods=['POST'])
# def format_css_route():
#     if 'css_text' in request.form:
#         css_text = request.form['css_text']
#         formatted_css = cssbeautifier.beautify(css_text)
#         return formatted_css
#     else:
#         return 'Please provide CSS text to format.', 400
from flask import Blueprint, request, send_file
from tempfile import NamedTemporaryFile
import cssbeautifier

format_css = Blueprint('format_css', __name__)

@format_css.route('/format-css', methods=['POST'])
def format_css_route():
    if 'css_file' not in request.files:
        return 'No CSS file uploaded', 400

    css_file = request.files['css_file']

    if css_file.filename == '':
        return 'No selected file', 400

    if css_file:
        css_text = css_file.read().decode('utf-8')
        formatted_css = cssbeautifier.beautify(css_text)

        # Create a temporary file to store the formatted CSS
        temp_file = NamedTemporaryFile(delete=False, suffix='.css')
        temp_file.write(formatted_css.encode('utf-8'))
        temp_file.close()

        # Return the formatted CSS file as a response
        return send_file(temp_file.name, as_attachment=True, download_name='formatted_css.css')
    
    return 'Error processing CSS file', 500
