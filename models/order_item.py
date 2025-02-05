from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class OrderItem(models.Model):
    _name = 'order.item'
    _description = "Order Item"
    _rec_name = 'meal_id'

    order_id = fields.Many2one('meal.order', string="Order", readonly=True, copy=False)
    meal_id = fields.Many2one('order.meal', string="Meal", copy=False)
    total_price = fields.Float("Total Price", compute="_compute_total_price")
    quantity = fields.Float("Quantity")
    price = fields.Float("Price")
    state = fields.Selection([], related="order_id.state")

    @api.onchange('meal_id')
    def set_price(self):
        if self.meal_id:
            self.price = self.meal_id.price

    # @api.onchange('price', 'quantity')
    # def _compute_price(self):
    #     self.total_price = self.quantity * self.price

    @api.depends('price', 'quantity')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.price * record.quantity

    @api.constrains('price')
    def check_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Price Must be bigger than zero")