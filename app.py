from flask import Flask, render_template, request, jsonify, send_file
import os
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from config import CSV_FILE, EXCEL_FILE, XML_FILE
from convert_data import convert_to_csv, convert_to_excel, convert_to_xml

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'No city provided'}), 400

    raw_data = fetch_weather_data(city)
    if 'error' in raw_data:
        return jsonify(raw_data), 404
        
    result = process_weather_data(raw_data)
    
    # Save files for download
    convert_to_csv(result['df'])
    convert_to_excel(result['df'])
    convert_to_xml(result['df'])

    return jsonify(result['display'])

@app.route('/download/<file_type>')
def download(file_type):
    paths = {'csv': CSV_FILE, 'excel': EXCEL_FILE, 'xml': XML_FILE}
    target = paths.get(file_type)
    if target and os.path.exists(target):
        return send_file(target, as_attachment=True)
    return "File not found. Search for a city first.", 404

if __name__ == "__main__":
    app.run(debug=True)