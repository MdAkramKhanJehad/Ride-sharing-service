import time
import  requests
from flask_socketio import SocketIO
from flask import Flask, request
from threading import Timer
from flask_apscheduler import APScheduler
import eventlet
from flask_mongoengine import MongoEngine
import json



eventlet.monkey_patch()
scheduler = APScheduler()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'its secret'
app.config['MONGODB_SETTINGS'] = {
    'db': 'ride_sharing_app',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)
socketio = SocketIO(app)

drivers = []
riders = []



@socketio.on('message')
def get_a_car(rider):
    selected_driver = None
    selected_dist = 999999

    for driver in drivers:
        point1 = str(driver['location']).split(",")
        point2 = str(rider['source']).split(",")
        distance = pow(pow(int(point1[0]) - int(point2[0]), 2) + pow(int(point1[1]) - int(point2[1]), 2), 0.5)
        
        if distance < selected_dist:
            selected_driver = driver
            selected_dist = distance

    return selected_driver, selected_dist


@app.route('/driver', methods=['POST'])
def driver():
    data = request.json
    drivers.append(data)
    return data


@app.route('/rider', methods=['POST'])
def rider():
    data = request.json
    riders.append(data)
    return data


@app.route('/rating', methods=['POST'])
def rating():
    data = request.json
    print("Rating:", data)
    r = requests.post("http://localhost:7000/rating", json=json.dumps(data))
    # insert_into_database(data['driver'], data['rating']) 

    return "rating completed"



def find_a_driver():
    print(time.strftime("%I:%M:%S %p"))
    if len(drivers) > 0 and len(riders) > 0:
        driver, distance = get_a_car(riders[0])
        socketio.emit('message', [riders[0]['Rider'], driver['Driver'], round(distance * 2)], namespace='/communication')
        riders.pop(0)

   

if __name__ == '__main__':
    scheduler.add_job(id='Schedule task', func=find_a_driver, trigger='interval', seconds=5)
    scheduler.start()
    socketio.run(app, port=8000)
