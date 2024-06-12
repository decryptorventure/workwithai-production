from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/home', methods=['GET'])
def return_home():
    return jsonify({
        'message': "Work with AI",
        'people' : ['Tom ','Trang ','Be Na']
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)