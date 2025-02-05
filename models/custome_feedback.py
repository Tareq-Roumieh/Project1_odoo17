from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomerFeedback(models.Model):
    _name = 'customer.feedback'
    _description = "Customer Feedback"

    name = fields.Char("Name", required=True)
    comment = fields.Char("Comment")
    reason = fields.Char("Reason", readonly=True)
    rate = fields.Selection([('0','0'), ('1','1'), ('2','2'), ('3','3')], string="Rate")
    customer_id = fields.Many2one('res.partner', string="Customer")
    meal_id = fields.Many2one('order.meal', string="Meal", copy=False)
    state = fields.Selection([('new', 'New'), ('approved', 'Approved'), ('rejected', 'Rejected')],
                             default='new', string="State", readonly=True)

    def action_approved(self):
        self.state = 'approved'