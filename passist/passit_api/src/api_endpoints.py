from flask import Flask
from flask_restful import Resource, Api
from web_spiders import *




app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, '/')
api.add_resource(WebSpider, '/<string:spider_name>')

if __name__ == '__main__':
    app.run(debug=True)

