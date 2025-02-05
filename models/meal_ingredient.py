from odoo import models, fields

# مكون الوجبة
class MealIngredient(models.Model):
    _name = 'meal.ingredient'
    _description = "Meal Ingredient"

    name = fields.Char("Name", required=True)
    product_id = fields.Many2one('product.product', string="product",
                                 domain="[('detailed_type', '=','product')]")
    meal_id = fields.Many2one('order.meal', string="Meal", copy=False)
    quantity = fields.Float("Quantity")