# -*- coding: utf-8 -*-
{
    'name': "contabilidad",

    'summary': """
      Borre lo que habia aqui, me tiraba un error xd
      .""",

    'description': """
        Modulo encargado de la contabilidad del negocio.
    """,

    'author': "Roberto Antonio Muñoz Campos",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Contabilidad',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
