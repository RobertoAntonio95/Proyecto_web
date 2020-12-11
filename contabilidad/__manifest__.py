# -*- coding: utf-8 -*-
{
    'name': "contabilidad",

    'summary': """
        El modulo de contabilidad esta diseñado exclusivamente para la simplicación de
        procesos financieros tales como balances y la facturación del negocio. La automatización
        de este modulo permitirá una facturación rápida y ágil creando cierres
        contables en plazos determinados de tiempo. Por último, este módulo permite de
        forma rápida y sencilla enviar las facturas correspondiente a los clientes vía correo
        electrónico al momento de que estos paguen, además de almacenarlas en la base de
        datos para futuros análisis.""",

    'description': """
        Modulo encargado de la contabilidad del negocio.
    """,

    'author': "Roberto Antonio Muñoz Campos",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'category': 'Contabilidad',
    'version': '1,1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_cargo.xml',
        'views/views_vendedor.xml',
        'views/views_facturas.xml',
        'views/views_banco.xml',
        'views/views_detalle.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
