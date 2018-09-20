from odoo import api, fields, models
from odoo.addons.base.res.res_request import referenceable_models

class TodoTask(models.Model):
    _name = 'todo.task' # prototype inheritance <= using along [_inherit, _name]
    _inherit = ['todo.task', 'mail.thread']
    name = fields.Char(help="What needs to be done?")
    effort_estimate = fields.Integer()
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many(
        'todo.task.tag',        # related model
        'todo_task_tag_rel',    # relation table name
        'task_id',              # field for "this" model
        'tag_id',               # field for "other" record
        string='Tags')          # string label text
    # refers_to = fields.Reference(
    #    [('res.user', 'User'), ('res.partner', 'Partner')],
    #    'Refers to')
    refers_to = fields.Reference(
        referenceable_models, 'Refers to')
    
    # Computed field
    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute='_compute_stage_fold',
        # store=False, # the default
        search='_search_stage_fold',
        inverse='_write_stage_fold')
    
    state = fields.Selection(
        related='stage_id.state',
        string='Stage State')
    
    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='_compute_user_todo_count')
    
    effort_estimate = fields.Integer('Effort Estimate')
    
    color = fields.Integer('Color Index')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority',
        default='1')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')],
        'Kanban State',
        default='normal')
    
    _sql_constraints = [
        ('todo_task_name_uniq',     # Constraint unique indentifier
         'UNIQUE(name, active)',    # Constraint SQL syntax
         'Task title must be unique!') # Validation message
    ]
    
    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for todo in self:
            todo.stage_fold = todo.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]
    
    def _write_stage_fold(self):
        for todo in self:
            todo.stage_id.fold = todo.stage_fold
            
    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Must have 5 chars!')
    
    def _compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count([('user_id', '=', task.user_id.id)])
    