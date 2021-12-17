import os
import json
from flask import Flask
from datetime import timedelta 



def loadConfig(app):
    app.config['ENV'] = os.environ.get('ENV', 'development')
    if app.config['ENV'] == "development":
 #       app.config.from_object('App.config')
        pass
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] = os.environ.get('JWT_EXPIRATION_DELTA')
        app.config['DEBUG'] = os.environ.get('DEBUG')
        app.config['ENV'] = os.environ.get('ENV')






def create_app():
    app = Flask(__name__)
    loadConfig(app)
   
    return app


app = create_app()
app.app_context().push()



@app.route('/', methods=["GET"])
def test():
    return "string"

if __name__ == '__main__':
    print('Application running in '+app.config['ENV']+' mode')
    app.run(host='0.0.0.0', port=8080, debug=app.config['ENV']=='development')