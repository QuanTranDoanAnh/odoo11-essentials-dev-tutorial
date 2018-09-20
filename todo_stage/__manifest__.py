{
    'name': 'Add Stages and Tags to To-Dos',
    'description': 'Organize To-Do Tasks using Stages and Tags',
    'author': 'QuanTDA1',
    'depends': ['todo_app', 'mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/todo_kanban_view.xml',
        'reports/todo_report.xml',
        'reports/todo_task_report.xml'
    ],
    'demo': [
        'data/todo.task.csv',
        'data/todo_task.xml',
    ]
}