from odoo import models, fields


class MealCategory(models.Model):
    _name = "order.meal.category"
    _description = "Order Meal Category"
    _order = "name"
    # _rec_name = "test"

    name = fields.Char("Name", required=True)


class Meal(models.Model):
    _name = "order.meal"
    _description = "Order Meal"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    price = fields.Float("Price", copy=False)
    category_id = fields.Many2one("order.meal.category", string="Category",ondelete="restrict")# cascade
    ingredient_ids = fields.One2many('meal.ingredient', 'meal_id', string="Ingredients")


    def action_view_feedback(self):
        # select  --> search
        # * --> ----
        # from --> self.env['MODEL-NAME']
        # where --> domain=[()]

        feedback_ids = self.env['customer.feedback'].search([('meal_id', '=', self.id)])
        return {
            'type': 'ir.actions.act_window',
            'name': "FeedBacks",
            'view_mode': "tree",
            'res_model': 'customer.feedback',
            'target': 'current',
            'domain': [('id', 'in', feedback_ids.ids)],
            'context': {'default_meal_id': self.id}
        }
        #self.feedback_ids.ids