# -*- coding: utf-8 -*-
{
    'name': "tech_order1",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Tareq Abbas Roumieh",
    'website': "https://www.linkedin.com/in/tareq-roumieh-71a64b2b4?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/meal.xml',
        'wizards/add_external_item.xml',
        'views/order.xml',
        'views/order_tag.xml',
        'views/meal_ingredient.xml',
        'wizards/feedback_reason.xml',
        'views/custome_feedback.xml',
        'views/external_item.xml',
        'data/server_actions.xml',
        'data/scheduale_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}