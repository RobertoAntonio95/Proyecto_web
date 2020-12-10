# -*- coding: utf-8 -*-
{
    'name': "inventario",

    'summary': """
        Inventario permite llevar fácilmente un preciso control de las
        entradas y salidas de mercadería durante el proceso de compra por parte del cliente,
        así como también, manejar adecuadamente los niveles de inventario y entregar toda
        la información para la administración de éstos. En esta ocasión, es gran importancia
        para "Fachy Comercial" tener la información acerca de la cantidad de inventario
        disponible en la bodegas, pero más aún, es vital para la supervivencia del negocio
        tener herramientas que ayuden a evitar o inhibir la pérdida, extravío o merma de
        los productos en inventario.""",

    'description': """
        Modulo encargado del manejo de mercadería del negocio
    """,

    'author': "Matías Rodríguez Morán",
    'website': "http://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'inventario',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/categoria.xml',
        'views/proveedor.xml',
        'views/producto.xml',
        'views/presupuesto.xml',
        'views/detalle_presupuesto.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
