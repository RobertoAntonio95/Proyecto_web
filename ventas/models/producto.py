from odoo import models, fields, api

class Producto(models.Model):

    _name = 'ventas.producto'
    _description = 'productos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)
    descripcion = fields.Char(string="descripcion", required=True)
    stock = fields.Integer(string="stock")
    stock_critico = fields.Integer(string="stock_critico")
    impuesto = fields.Integer(string="impuesto")    # PENSANDO QUE NO FUERA UN VALOR ENTERO
    precio_unitario = fields.Integer(string="precio_unitario")
    preciofinal = fields.Integer(string="preciofinal")
    
    apo_id = fields.Many2one('ventas.detalle_compra', string='Apo ID') 

    #FK ID DEL PROVEEDOR

 