from odoo import models, fields, api

class detalle_compra(models.Model):
    _name = 'ventas.detalle_compra'
    _description = 'Detalles de la compra'

    cantidad = fields.Char(string="Cantidad de Productos", required=True)
    precio_costo = fields.Many2one('ventas.ordencompra',string="Precio", required=True)

  
    precio_total = fields.Char(string="Precio Total", required=True)
    impuestos = fields.Char(string="IVA", required=True)
   # id_producto = fields.Many2one()

  