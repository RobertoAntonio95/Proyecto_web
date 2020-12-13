# -*- coding: utf-8 -*-
{
    'name': "Ventas-IIE",

    'summary': """
        Este módulo estará encargado de las ventas del sistema, el cual presentara al cliente
        interno o responsable los productos a vender.""",

    'description': """
        Modulo encargado de las ventas a clientes mayoristas del negocio
    """,

    'author': "Tomás Navarro Mancilla",
    'website': "http://www.Utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ventas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_cliente.xml',
        'views/view_ordencompra.xml',
        'views/view_detalle_orden_compra.xml',
    ],
    'application': True
}
