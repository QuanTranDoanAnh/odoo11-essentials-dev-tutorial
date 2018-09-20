from odoo import http
from odoo.http import request

class Todo(http.Controller):
    
    @http.route('/helloworld', auth='public')
    def hello_world(self):
        return ('<h1>Hello World</h1>')
    
    @http.route('/hello', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render('todo_website.hello')
    
    @http.route('/hellocms/<page>', auth='public', website=True)
    def hellocms(self, page, **kwargs):
        return request.render(page)
    
    @http.route('/todos', auth='user', website=True)
    def index(self, **kwargs):
        TodoTask = request.env['todo.task']
        tasks = TodoTask.search([])
        return request.render(
            'todo_website.index',
            {'tasks': tasks})
        
    @http.route('/todo/<model("todo.task"):task>',
                auth='user', # default, but made explicit here
                website=True)
    def detail(self, task, **kwargs):
        return request.render(
            'todo_website.detail',
            {'task': task})
    
    @http.route('/todo/add', auth='user', website=True)
    def add(self, **kwargs):
        users = request.env['res.users'].search([])
        return request.render(
            'todo_website.add',
            {'users': users})