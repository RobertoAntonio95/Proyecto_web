from odoo import models, fields, api




class detalle_compra(models.Model):
    _name = 'ventas.detalle_compra'
    _description = 'Detalles de la compra'

    cantidad = fields.Char(string="Fecha de compra", required=True)
    precio_costo = fields.One2many('ventas.ordencompra',string="Fecha de compra", required=True)

  
    precio_total = fields.Char(string="Fecha de compra", required=True)
    impuestos = fields.Char(string="Fecha de compra", required=True)
   # id_producto = fields.Many2one()
    