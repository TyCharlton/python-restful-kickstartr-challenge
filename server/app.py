from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Project, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Note: app.json.compact = False #Configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


class Projects(Resource):

    def get(self):
        projects = [project.to_dict() for project in Project.query.all()]
        body = projects
        status = 200

        return make_response(body, status)
    
    def post(self):
        data = request.get_json()
        # new_project = Project()
        # for key, value in data.items():
        #     setattr(new_project, key, value)
        new_project = Project(
            title=data["title"],
            creator=data["creator"]
        )
        db.session.add(new_project)
        db.session.commit()
        return make_response(new_project.to_dict(), 200)

api.add_resource(Projects, '/')

class ProjectByID(Resource):
    def get(self, id):
        project = Project.query.filter(Project.id == id).first()

        return make_response(project.to_dict(), 200)

    def patch(self, id):
        project = Project.query.filter(Project.id == id).first()

        if not project:
            return make_response({'error':'nope, bye'}, 404)

        data =  request.get_json()
        for key, value in data.items():
            setattr(project, key, value)
        db.session.commit()

        return make_response(project.to_dict(), 202)
    
    def delete(self, id):
        project = Project.query.filter(Project.id == id).first()

        if not project:
            return make_response({'This is nor found, bye'}, 404)

        db.session.delete(project)
        db.session.commit()

        return make_response({}, 204)
    

api.add_resource(ProjectByID, '/<int:id>')

if __name__ == "__main__":
    app.run(port=5555, debug=True)