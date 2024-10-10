from flask_restful import Resource

class ViewPing(Resource):
    def get(self):
        return "pong",200


        