from odoo import models, fields, api


class Detalle(models.Model):

    _name = 'contabilidad.detalle'
    _description = 'detalles de facturas'
    _rec_name = 'factura_id'

    factura_id = fields.Many2one('contabilidad.factura', string="factura_id")
    producto_id = fields.Many2one(
        'inventario.producto', string="producto_id")

    cantidad = fields.Integer(string="cantidad", required=True, default="1")
    total = fields.Integer(string="total", compute="_get_precio")

    @api.one
    def _get_precio(self):
        self.total = (self.cantidad * self.producto_id.precio_venta)
