from flask import Flask, render_template, jsonify, request
import Controller
import asyncio

app = Flask(__name__)
control = Controller.Controller()


@app.route('/api/generate', methods=['GET'])
def new_params():
    control.generate_data()
    stats = control.get_stats()
    # Оновлення значень чер, pollution)
    return jsonify({
        "temperature": stats[0],
        "humidity": stats[1],
        "pollution": stats[2]
    })


@app.route('/api/update', methods=['GET'])
async def update_params():
    updated_stats = await control.update_all()
    # Оновлення значень чер, pollution)
    return jsonify({
        "temperature": updated_stats[0],
        "humidity": updated_stats[1],
        "pollution": updated_stats[2]
    })


@app.route('/api/get_data', methods=['GET'])
def get_sensor_data():
    data = control.get_stats()
    response = {
        "pollution": data[2],
        "humidity": data[1],
        "temperature": data[0],
    }
    return jsonify(response)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
