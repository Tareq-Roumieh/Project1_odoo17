from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class ExternalItemWizard(models.TransientModel):
    _name="external.item.wizard"
    _description = "External Item Wizard"

    _transient_max_count = 3
    _transient_max_hours  = 3

    def set_default_item(self):
        items = self.env['external.item'].search([])
        return items

    external_item_ids = fields.Many2many('external.item', string="External items",
                                         default=set_default_item)

    def add_items(self):
        order = self.env["meal.order"].browse(self.env.context.get("active_id"))
        # order.update({"external_item_ids": self.external_item_ids.ids})
        order.update({'external_item_ids':[(4,item.id) for item in self.external_item_ids]})
