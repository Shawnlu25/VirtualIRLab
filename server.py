from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from schema import db, redis_store
from api.searchAPI import SearchAPI
from api.annotationAPI import AnnotationAPI
from api.uploadAPI import UploadAPI
from api.userAPI import UserAPI, LoginAPI
from api.assignmentAPI import AssignmentAPI, AddQueryAPI
from api.instructorAPI import InstructorAPI
from api.classAPI import ClassAPI

from util.exception import InvalidUsage

from flask import render_template

app = Flask(__name__, static_folder='static/', static_url_path='')
app.config.from_object('config')
api = Api(app)
CORS(app)

db.init_app(app)
redis_store.init_app(app)

api.add_resource(SearchAPI, '/search/<string:author>/<string:ds_name>')
api.add_resource(AnnotationAPI, '/annotation')
api.add_resource(UploadAPI, '/upload')
api.add_resource(UserAPI, '/register')
api.add_resource(LoginAPI, '/login')
api.add_resource(AssignmentAPI, '/assign')
api.add_resource(AddQueryAPI, '/newquery')
api.add_resource(InstructorAPI, '/instructor')
api.add_resource(ClassAPI, '/class')

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response

@app.route("/student")
def student_page():
	return render_template("student.html")

@app.route("/index")
def main():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(host='127.0.0.1')
