from odoo import models, fields, api


class Detalle_presupuesto(models.Model):

    _name = 'inventario.detalle_presupuesto'
    _description = 'detalle de presupuestos'
    _rec_name = 'descripcion'

    cantidad = fields.Integer(string="Cantidad", required=True)
    precio_unitario = fields.Integer(string="Precio Unitario", required=True)
    impuesto = fields.Boolean(string="IVA", required=True)
    total = fields.Integer(string="Total", required=True)
    descripcion = fields.Char(string="ID", required=True)
  
    # ACÁ LAS FK QUE UTILIZAREMOS DESDE LAS OTRAS TABLAS
    producto_id = fields.Many2one('inventario.producto', string='Producto')