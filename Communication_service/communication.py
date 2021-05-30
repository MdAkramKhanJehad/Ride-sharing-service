from flask import Flask,request,g
from flask_socketio import SocketIO,emit
import json, eventlet


eventlet.monkey_patch()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'its secret'
socketio = SocketIO(app)



@app.route('/newPair', methods=['POST'])
def rider():
    data = request.json
    x = json.loads(data)
    print(x)
    communicate(x)
    return data



@socketio.on('message')
def communicate(data):
	data = [data['rider'], data['driver'], data['fare']]   
	socketio.emit('message', data, namespace='/communication')


if __name__ == '__main__':
    socketio.run(app,port=6000)



