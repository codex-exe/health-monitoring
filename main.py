from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load your JSON dataset
with open("./dataset.json", 'r') as file:
    dataset = json.load(file)

@app.route('/get_data', methods=['GET'])
def get_data():
    user = str(request.args.get('user'))
    time = str(request.args.get('time'))

    flag = 1
    if user in dataset.keys():
        for i in dataset[user]:
            if i['time'] == time:
                flag = 1
                return jsonify(i)
            else:
                flag = 0
        if flag == 0:
            return("No data found!")
    else:
        return("User not found!")

    return "404"

if __name__ == '__main__':
    app.run(debug=True)