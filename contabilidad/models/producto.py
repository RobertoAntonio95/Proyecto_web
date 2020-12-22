from odoo import models, fields, api


class Producto(models.Model):

    _name = 'contabilidad.producto'
    _description = 'productos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    marca = fields.Char(string="Marca", required=True)
    stock = fields.Integer(string="Stock", required=True)
    stock_critico = fields.Integer(string="Stock Crítico", required=True)
    precio_costo = fields.Integer(string="Precio Costo", required=True)
    precio_venta = fields.Integer(string="Precio Venta", required=True)

    producto_id = fields.One2many(
        'contabilidad.detalle', 'producto_id', string='producto_id')
