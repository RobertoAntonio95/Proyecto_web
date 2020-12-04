# -*- coding: utf-8 -*-
{
    'name': "Ventas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       Ejemplo de desarrollo de modulo de ventas en odoo
    """,

    'author': "Tomas Navarro",
    'website': "www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
       # 'security/ir.model.access.csv',
        'views/view_ventas.xml',
       # 'views/templates.xml',
    ],
   
}