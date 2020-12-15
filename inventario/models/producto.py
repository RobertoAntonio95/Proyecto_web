from odoo import models, fields, api


class Producto(models.Model):

    _name = 'inventario.producto'
    _description = 'productos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    marca = fields.Char(string="Marca", required=True)
    stock = fields.Integer(string="Stock")
    stock_critico = fields.Integer(string="Stock Crítico")
    impuesto = fields.Boolean(string="IVA")
    precio_unitario = fields.Integer(string="Precio Unitario")
    precio_final = fields.Integer(string="Precio Final")

    # FK ID DEL PROVEEDOR

    proveedor_id = fields.Many2one(
        'inventario.proveedor', string="ID Proveedor")
