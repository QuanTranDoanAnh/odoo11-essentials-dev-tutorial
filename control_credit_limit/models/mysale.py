from odoo import api, models, fields
from odoo.exceptions import UserError
from odoo import exceptions

class MySale(models.Model):
    _inherit = "sale.order"
    
    @api.multi
    def check_credit_limit(self):
        self.ensure_one()
        partner = self.partner_id
        all_invoices = self.env['account.invoice'].search([
            ('partner_id', '=', partner.id),
            ('type', '=', 'out_invoice'),
            ('company_id', '=', self.company_id.id),
            ('state', 'in', ['open'])
        ])
        all_open=0
        all_due=0.0
        for inv in all_invoices:
            due = inv.residual
            all_due += due
            all_open += 1
        new_balance = self.amount_total + partner.credit
        msg = 'Credit Limit Error !! You need to increase the limit of this customer to proceed \n New Balance %s \n Current Customer Balance %s \n Limit %s \n Open Invoices %s \n Due Invoices %s ' % (new_balance, (partner.credit*(-1)), partner.my_credit_limit, all_open, all_due)
        
        if new_balance > partner.my_credit_limit:
            raise exceptions.ValidationError(msg)
        else:
            return True
    
    @api.multi
    def action_confirm(self):
        for order in self:
            order.check_credit_limit()
        res = super(MySale, self).action_confirm()
        return res