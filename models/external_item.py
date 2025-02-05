from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class ExternalItem(models.Model):
    _name = 'external.item'
    _description = "External Item"
    _rec_name = "product_id"

    product_id = fields.Many2one('product.product', string="Product")