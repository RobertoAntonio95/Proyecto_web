# -*- coding: utf-8 -*-
{
    'name': "contabilidad",

    'summary': """
        El modulo de contabilidad esta dise~nado exclusivamente para la simplicacion de
procesos nancieros tales como balances y la facturacion del negocio. La automatizaci
on de este modulo permitira una facturacion rapida y agil creando cierres
contables en plazos determinados de tiempo. Por ultimo, este modulo permite de
forma rapida y sencilla enviar las facturas correspondiente a los clientes va correo
electronico al momento de que estos paguen, ademas de almacenarlas en la base de
datos para futuros analisis.""",

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
