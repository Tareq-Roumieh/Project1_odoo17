from odoo import models, fields

class OrderTag(models.Model):
    _name = 'order.tag'
    _description = "Order Tag"

    name = fields.Char("Name", requiered=True)
    color = fields.Integer("Color")
    # order_ids = fields.Many2many('meal.order', "Order")