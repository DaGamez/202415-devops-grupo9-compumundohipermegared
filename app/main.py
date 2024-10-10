import os
from flask import Flask,jsonify,request
from flask_restful import Api
import datetime
import logging
from models.models import db
from views.ping import ViewPing
from views.blacklist import ViewBlacklist
import time
from sqlalchemy.exc import OperationalError

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# en caso de no encontrar variables de entorno se asume que se está en ambiente de desarrollo
# y por lo tanto se busca una bd postgres corriendo en local con configuraciones de default

db_user=os.getenv('DB_USER', 'postgres')
db_password=os.getenv('DB_PASSWORD', 'postgres')
db_name=os.getenv('DB_NAME', 'postgres')
db_port=os.getenv('DB_PORT', '5432')
db_host=os.getenv('DB_HOST', 'localhost')

def add_resources_urls(app):
    '''
    se especifican las rutas de los recursos
    recibe como input un app de la forma app = Flask(__name__) 
    '''
    api = Api(app)
    api.add_resource(ViewPing, '/ping')
    api.add_resource(ViewBlacklist, '/blacklists', '/blacklists/<string:email>')




def create_flask_app(db_dir):
    app = Flask(__name__)   
    app.config['SQLALCHEMY_DATABASE_URI'] = db_dir
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    max_retries = 5
    retry_delay = 5

    with app.app_context():
        for attempt in range(max_retries):
            try:
                db.create_all()
                break
            except OperationalError as e:
                if attempt < max_retries - 1:
                    print(f"Database connection attempt {attempt + 1} failed. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print("Failed to connect to the database after multiple attempts.")
                    raise e
    
    add_resources_urls(app)

    return app


app= create_flask_app(db_dir=f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

if __name__ == '__main__':
    app.run(debug=True)