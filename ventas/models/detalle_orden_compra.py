from odoo import models, fields, api


class detalle_compra(models.Model):
    _name = 'ventas.detalle_compra'
    _description = 'Detalles de la compra'
    _rec_name = 'ordencompra_id'

    ordencompra_id = fields.Many2one(
        'ventas.ordencompra', string="Orden compra ID")

    producto_id = fields.Many2one('inventario.producto', string='Producto ID')

    id_vendedor = fields.Many2one(
        'contabilidad.vendedor', string='Vendedor encargado')

    cantidad = fields.Integer(string="cantidad", required=True, default="1")

    precio_total = fields.Integer(string="total", compute="_get_precio")

    @api.one
    def _get_precio(self):
        self.precio_total = (self.cantidad * self.producto_id.precio_venta)

    total = fields.Float('TOTAL')
