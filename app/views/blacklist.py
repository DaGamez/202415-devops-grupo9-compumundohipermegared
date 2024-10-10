from flask import request,jsonify
from flask_restful import Resource
from models.models import ListaNegraEmails,ListaNegraEmailsSchema,db
from datetime import datetime
from marshmallow import fields, Schema
from uuid import uuid4
import os
import requests
import uuid

class ViewBlacklist(Resource):
    def get(self, email=None):
        if email:
            blacklist_item = ListaNegraEmails.query.filter_by(email_lista_negra=email).first()
            if blacklist_item:
                blacklist_schema = ListaNegraEmailsSchema()
                return 'true',200
            else:
                return 'false',200
        else:
            return "", 404

    #endpoing creacion de item en lista negra
    def post(self):
        data = request.json
        email = data.get('email')
        app_uuid = data.get('app_uuid')
        blocked_reason = data.get('blocked_reason')
        ip_origen_solicitud = request.remote_addr 

        # Check if the email already exists in the blacklist
        existing_item = ListaNegraEmails.query.filter_by(email_lista_negra=email).first()
        if existing_item:
            return {'message': 'Email already in blacklist'}, 409

        blacklist_item = ListaNegraEmails(
            email_lista_negra=email,
            id_app_cliente_uuid=app_uuid,
            motivo_lista_negra=blocked_reason,
            ip_origen_solicitud=ip_origen_solicitud
        )
        # Add the new item to the database
        db.session.add(blacklist_item)
        db.session.commit()

        # Return the created item
        message = f'Email {email} added to blacklist'
        return {"message":message}, 201