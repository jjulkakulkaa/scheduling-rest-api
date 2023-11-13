from flask import Flask
from flask_restful import Resource, Api

app = Flask("SheduingAPI")
api = Api(app)

tasks = {
    'task1': {'title': 'Walk the dog'},
    'task2': {'title': 'Make dinner'}
}

class Task(Resource):
    def get(self, task_id):
        if task_id == "all":
            return tasks
        return tasks[task_id]
    
    def put(self, )
    
api.add_resource(Task, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run()