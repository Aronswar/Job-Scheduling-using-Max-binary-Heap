from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from timestam import *

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('Rainbowsprinkle', description='API for Job scheduling')




a_id=api.model('Job ID',{'ID_of': fields.Integer(max=9223372036854775807, description='ID provided'),'Time1': fields.Integer("Time in seconds")})
a_time=api.model('Time Now',{'Time_nw': fields.Integer()})
a_new=api.model('New Id',{'ID_now' : fields.Integer(description='enter your job ID')})

class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        return {"Avg_wait":(time_of_Avgwait(id)*(-1))}
        api.abort(404, "Job {} doesn't exist".format(id))

    def delete(self, id):
        return {"result": "Deleted"}

class list_t(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
         return{"position":(findin_index_value(id))}
         api.abort(404, "Job {} doesn't exist".format(id))

@ns.route('/listAlltheJobs')
class LsItems(Resource):
    def get(self):
        return q

@ns.route('/addJobs')
class jobAdd(Resource):

    @ns.expect(a_id)
    def post(a_id):
        newva=api.payload
        return {'result': get_value_and_timestamp(newva['ID_of'],newva['Time1'])}

DAO=TodoDAO()
NEO=list_t()

@ns.route('/<int:id>')
@ns.response(404, 'Job not found')
@ns.param('id', 'TIme in seconds')
class Todo(Resource):

    @ns.doc('get_todo')
    #@ns.marshal_with(todo)
    def get(self, id):
        '''Fetch Average time'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204


@ns.route('indexval/<int:id>')
@ns.response(404, 'Job not found')
@ns.param('id', 'The task identifier')
class Indelo(Resource):
    @ns.doc('get_todo')
    def get(self, id):
        '''Fetch the indexPosition'''
        return NEO.get(id)

@ns.route('/topvalue')
class Removetop(Resource):
    def get(self):
        '''Removing the top value'''
        vale=top_most_item()
        return vale

if __name__ == '__main__':
    app.run(debug=True)
