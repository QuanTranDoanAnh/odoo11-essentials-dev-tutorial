{
    'name': 'To-Do Website',
    'description': 'To-Do Tasks Website',
    'author': 'QuanTDA1',
    'application': True,
    #'depends': ['todo_stage', 'website'],
    'depends': ['todo_stage', 'website_form'],
    'data': [
        'views/todo_web.xml',
        'views/todo_extend.xml',
        'data/config_data.xml'
    ]
}