from flask import Flask, request, jsonify
# init app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'msg': 'Hello world'})


# Run server
if __name__ == "__main__":
    app.run(debug=True)
