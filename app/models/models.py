import enum
from sqlalchemy import UniqueConstraint,and_
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import backref

db = SQLAlchemy()

class ListaNegraEmails(db.Model):
    __tablename__ = 'lista_negra_emails'
    email_lista_negra = db.Column(db.String(100), primary_key=True)
    id_app_cliente_uuid = db.Column(db.String(36), nullable=False)
    motivo_lista_negra = db.Column(db.String(255), nullable=False)
    ip_origen_solicitud = db.Column(db.String(30), nullable=False)
    fecha_solicitud = db.Column(db.DateTime, default=db.func.current_timestamp())

class ListaNegraEmailsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ListaNegraEmails
        include_relationships = True
        load_instance = True