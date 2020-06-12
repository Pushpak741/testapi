from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.emp import Emp,Emplogin

app=Flask(__name__)
app.config['JWT_SECTRET_KEY']='coscskillup'
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['PREFERRED_URL_SCHEME']='https'
api=Api(app)
jwt=JWTManager(app)

api.add_resource(Emp,'/emp')
api.add_resource(Emplogin,'/login')

if __name__ == "__main__":
    app.run()
