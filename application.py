import os
from flask import Flask, jsonify
from flask_restful import Api
from app.models import db
from app.routes import api_bp

application = Flask(__name__)

db_user = os.getenv('RDS_USERNAME', 'blacklist')
db_password = os.getenv('RDS_PASSWORD', '%r&GRHJJu786')
db_host = os.getenv('RDS_HOSTNAME', 'localhost')
db_name = os.getenv('RDS_DB_NAME', 'ebdb')
db_port = os.getenv('RDS_PORT', '5432')

application.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(application)

# Crear las tablas en la base de datos
with application.app_context():
    db.create_all()

api = Api(application)

application.register_blueprint(api_bp)

@application.route('/')
def index():
    return jsonify({
        'message': 'Microservicio de lista negra de emails!',
        'status': 'success'
    })

if __name__ == "__main__":
    application.debug = True
    application.run()
