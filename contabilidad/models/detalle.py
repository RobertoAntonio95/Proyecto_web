from odoo import models, fields, api


class Detalle(models.Model):

    _name = 'contabilidad.detalle'
    _description = 'detalles de facturas'
    _rec_name = 'producto'

    producto = fields.Char(string="producto", required=True)
    cantidad = fields.Integer(string="cantidad", required=True, default="1")
    precio = fields.Integer(string="precio", required=True)
    total = fields.Integer(string="total", compute="_total")

    @api.one
    def _total(self):
        self.total = (self.cantidad * self.precio)

    factura_id = fields.Many2one('contabilidad.factura', string="factura_id")
