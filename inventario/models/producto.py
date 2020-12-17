from odoo import models, fields, api


class Producto(models.Model):

    _name = 'inventario.producto'
    _description = 'productos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    marca = fields.Char(string="Marca", required=True)
    stock = fields.Integer(string="Stock", required=True)
    stock_critico = fields.Integer(string="Stock Crítico", required=True)
    impuesto = fields.Boolean(string="IVA", required=True)
    precio_unitario = fields.Integer(string="Precio Unitario", required=True)
    precio_final = fields.Integer(string="Precio Final", required=True)

    # FK ID DEL PROVEEDOR

    proveedor_id = fields.Many2one(
        'inventario.proveedor', string="ID Proveedor")
