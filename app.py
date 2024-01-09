import os
from flask import Flask, render_template, request, jsonify
import requests 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    company_name = request.form['company_name']
    url = f"https://entreprise.data.gouv.fr/api/sirene/v1/full_text/{company_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Data not found"}), 404
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
