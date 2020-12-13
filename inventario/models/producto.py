from odoo import models, fields, api

class Producto(models.Model):

    _name = 'inventario.producto'
    _description = 'productos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)
    descripcion = fields.Char(string="descripcion", required=True)
    stock = fields.Integer(string="stock")
    stock_critico = fields.Integer(string="stock_critico")
    impuesto = fields.Integer(string="impuesto")    # PENSANDO QUE NO FUERA UN VALOR ENTERO
    precio_unitario = fields.Integer(string="precio_unitario")
    precio_final = fields.Integer(string="preciofinal")

    #FK ID DEL PROVEEDOR

    proveedor_id = fields.Many2one('inventario.proveedor', string="proveedor_id")
