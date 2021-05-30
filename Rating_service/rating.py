from flask import Flask,request,g
import json
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'its secret'

app.config['MONGODB_SETTINGS'] = {
    'db': 'driver_ratings',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)


class Rating(db.Document):
    driver = db.StringField()
    rating = db.StringField()


def insert_into_database(driver,rating):
    Rating(driver=driver, rating=rating).save()
    print("Records inserted........")


    # print('\n****************ALL RATINGs********************')
    
    ##find latest rating
    # driv = Rating.objects(driver=driver).first()
    # if not driv:
    #    print('not found')
    # else:
    #    print(driv.driver, ' ----- ', driv.rating)
    
    # find all ratings
    # for rate in Rating.objects:
    #     print(rate.driver,' -> ',rate.rating)
    
    #delete all the ratings
    # for rate in Rating.objects:
    #     rate.delete()
    #     print('*********deleted**********')
    
    print('\n')



@app.route('/rating', methods=['POST'])
def rating():
    data = request.json
    data = data
    insert_into_database(data['driver'], data['rating'])

    return data




if __name__ == '__main__':
	app.run(port=7000)