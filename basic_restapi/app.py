from flask import Flask, request, jsonify
app = Flask(__name__)

resource = []

@app.route('/user/<int:user_id>',methods =['GET'])
def get_user(user_id):
    for user in resource:
        if user['user_id'] is user_id:
            return jsonify(user)
    return jsonify(None)

@app.route('/user',methods=['POST'])
def add_user():
    user = request.get_json()
    print(user)
    resource.append(user)
    return jsonify()

if __name__ == '__main__':
    app.run()