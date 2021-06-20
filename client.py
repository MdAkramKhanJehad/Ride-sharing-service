import requests,json
import time
from threading import Timer
import socketio
import eventlet, random
import string
import string_utils

eventlet.monkey_patch()
sio = socketio.Client()
sio.connect('http://localhost:8080', namespaces=['/communication'])
print("Communication connceted")


riders = ["Akter", "Alam", "Rafin", "Kuddus", "Sakib", "Sahir", "Samnan", "Rizan", "Marzan", "Arifa",
               "Labiba", "Rahman", "Kalam"]
drivers = ["Samim", "Jabir", "Rafik", "Matin", "Omar", "Faruk", "Kashem", "Tomal", "Mahmud", "Siddik",
              "Didar", "Anis", "Liton"]



def get_random_point():
    a = str(random.randint(1, 1000))
    b = str(random.randint(1, 1000))
    return a + "," + b



@sio.event(namespace='/communication')
def message(data):
    print("\n\n****Got a Car:*****")
    print('Rider:',data[0],', Driver:', data[1],', Total Fare:',data[2],'\n\n')
    d = {"driver": data[1], "rating": str(random.randint(2, 5))}
    r = requests.post("http://localhost:10000/rating", json=d)



i = 1
while True:
    print(i)
    
    rider = {'Rider': random.choice(riders), 'source': get_random_point(), 'destination': get_random_point()}
    print('Rider ',rider['Rider'],' wanna go from ', rider['source'],' to ', rider['destination'])
    r = requests.post("http://localhost:10000/ridesharingservice/rider", json=rider)

    driver = {'Driver': random.choice(drivers), 'carNumber': str(random.randint(100001, 999999)), "location": get_random_point()}
    print('Driver ', driver['Driver'], ' is located at ', driver["location"], ', car number is ', driver['carNumber'])
    r = requests.post("http://localhost:10000/ridesharingservice/driver", json=driver)
    
    time.sleep(1.5)
    i += 1



time.sleep(1000)
