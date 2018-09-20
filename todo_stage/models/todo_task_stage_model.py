from odoo import fields, models

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence, name'
    # Stage class relationship with Tasks
    task_ids = fields.One2many(
        'todo.task', # related model
        'stage_id', # field for "this" on related model
        'Task in this stage')
    
    # String fields:
    name = fields.Char('Name', translate=True)
    desc = fields.Text('Description')
    state = fields.Selection(
        [('draft', 'New'),
         ('open', 'Started'),
         ('done', 'Closed')],
        'State')
    docs = fields.Html('Documentation')
    
    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    
    # Date fields
    date_effective = fields.Date('Effective Date')
    date_created = fields.Datetime(
        'Created Date and Time',
        default=lambda self: fields.Datetime.now())
    
    # Other fields
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')