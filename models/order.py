from odoo import models, fields, _, api
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class Order(models.Model):
    _name = "meal.order"
    _description = "Meal Order "
    _order = "name"


    def get_customer_domain(self):
        customers = self.env['res.partner'].search([('is_company', '=', True),
                                                    ('vat', '=', False)])
        return [('id', 'in', customers.ids)]



    name = fields.Char(string="Name", required=True,
                       default=lambda self: _('New'))
    total_price = fields.Float("Price", compute="_compute_total_price",
                               store=True, readonly=True)
    order_type = fields.Selection([('internal', 'Internal'), ('external', 'External')],
                                  string="Type", required=True,
                                  default="internal")
    note = fields.Text("NOTE")
    order_date = fields.Date("Order Date", copy=False, default=fields.datetime.now().date(),
                             readonly=False)
    customer_id = fields.Many2one("res.partner", string="Customer",
                                  domain=get_customer_domain)
    is_urgent = fields.Boolean("Is Urgent", copy=False)
    active = fields.Boolean(default=True)
    table_number = fields.Integer("Table Number")
    expected_duration = fields.Float("Expected Duration")
    expected_date = fields.Datetime("Expected Date", compute="_compute_expected_date",
                                    inverse="inverse_expected_date",
                                    readonly=False)

    order_tag_ids = fields.Many2many('order.tag', "Tags")
    item_ids = fields.One2many('order.item', 'order_id', string="Items")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('in_process', 'In Process'),
                              ('delivered', 'Delivered'),
                              ('cancelled', 'Cancelled'),
                              ],
                             string="State", default='draft')
    external_item_ids = fields.Many2many('external.item', string="External Item",
                                         readonly=True)

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Order Name already exists!'),
    ]

    @api.constrains('order_date')
    def check_order_date(self):
        for record in self:
            if record.order_date > datetime.now().date():
                raise ValidationError("Order Date Must be in present or past")

    @api.depends('item_ids', 'item_ids.total_price')
    def _compute_total_price(self):
        for record in self:
            total_price = 0
            for item in record.item_ids:
                total_price = total_price + item.total_price
            record.total_price = total_price

    @api.depends('order_date', 'expected_duration')
    def _compute_expected_date(self):
        for record in self:
            record.expected_date = record.order_date + timedelta(
                days=record.expected_duration)

    def inverse_expected_date(self):
        for record in self:
            record.expected_duration = (record.expected_date.date() - record.order_date).days



    def action_confirm(self):
        self.state = 'confirmed'
        self.order_date = datetime.now().date()

    def action_in_progress(self):
        self.state = 'in_process'

    def action_delivered(self):
        self.state = "delivered"

    def action_cancel(self):
        self.state = 'cancelled'

    def set_is_urgent(self):
        _logger.error("SELF ++ " + str(self))
        for rec in self:
            expected = rec.expected_date.date() - timedelta(days=1)
            _logger.error("expected ++ " + str(expected))
            _logger.error("datetime.now().date() ++ " + str(datetime.now().date()))
            if expected == datetime.now().date():
                rec.is_urgent = True


    def fetch_order(self):
        domain = [('state', 'in', ('confirmed', 'in_process')),
           '|', '&', ('order_type', '=', 'external'), ('expected_date', '<', datetime.now()),
         '&', ('order_type', '=', 'internal'), ('table_number', '=', 0)]
        orders = self.search([('state', 'in', ('confirmed', 'in_process')),
                              '|', '&', ('order_type', '=', 'external'), ('expected_date', '<', datetime.now()),
                              '&', ('order_type', '=', 'internal'), ('table_number', '=', 0)])
        # read_orders = orders.read(['name', 'order_type'])
        # orders = self.read_group([('state', 'in', ('confirmed', 'in_process')),
        #    '|', '&', ('order_type', '=', 'external'), ('expected_date', '<', datetime.now()),
        #  '&', ('order_type', '=', 'internal'), ('table_number', '=', 0)],
        #                          ['name', 'order_type'],
        #                          ['order_type', 'customer_id'],
        #                          lazy=False
        #
        #                         )

        # orders[1].unlink()
        # current_user = self.env.user
        # return orders