from flask_restful import Resource
from flask import request
from pymongo import Connection
import json
from bson import json_util


# MongoDB connection
connection = Connection('localhost', 27017)
db = connection.crawler

todos = {}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class WebSpider(Resource):
    def get(self, spider_name = ""):
        result = db['crawldata'].find_one({'spider_name': spider_name})
    	return self.toJson(result)
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
    def toJson(self, data):
		"""Convert Mongo object(s) to JSON"""
		return json.dumps(data, default=json_util.default)
