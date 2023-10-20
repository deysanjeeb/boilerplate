from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        # Handle GET request
        return jsonify({'message': 'GET request received'})
    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        # Process the data here
        result = {'message': 'POST request received', 'data': data}
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)