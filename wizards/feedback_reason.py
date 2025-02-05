from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class FeedbackReason(models.TransientModel):
    _name="feedback.reason"
    _description = "Feedback Reason"

    reason = fields.Char('Reason', required=True)

    def add_reason(self):
        #self.env['customer.feedback'].search([('id','=', self.env.context.get('active_id'))])
        feedback = self.env['customer.feedback'].browse(self.env.context.get('active_id'))
        feedback.update({'reason': self.reason, 'state': 'rejected'})

        # _logger.info("Hellow World " + str(self.env.context))