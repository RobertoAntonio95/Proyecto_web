from odoo import models, fields, api


class detalle_presupuesto(models.Model):

    _name = 'inventario.detalle_presupuesto'
    _description = 'detalle de presupuestos'
    _rec_name = 'descripcion'

# ACÁ LAS FK QUE UTILIZAREMOS DESDE LAS OTRAS TABLAS

   # producto_id = fields.Many2one(
   #     'inventario.producto', string='producto')


    cantidad = fields.Integer(string="Cantidad", required=True)
    precio_unitario = fields.Integer(string="precio_unitario", required=True)
    impuesto = fields.Integer(string="Impuesto", required=True)
    total = fields.Integer(string="Total", required=True)
    descripcion = fields.Char(string="Descripción", required=True)
  