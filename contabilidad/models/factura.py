from odoo import models, fields, api


class Factura(models.Model):

    _name = 'contabilidad.factura'
    _description = 'facturas'
    _rec_name = 'fecha_creación'

    vendedor_id = fields.Many2one(
        'contabilidad.vendedor', string='vendedor')
    banco_id = fields.Many2one(
        'contabilidad.banco', string='banco')

    #cliente = fields.Char('Title', required=True)
    fecha_creación = fields.Date("Fecha de creación de la factura")
    fecha_vencimiento = fields.Date("Fecha de vecimiento")
    # base imponible será la suma de todos los valores de los productos
    base_imponible = fields.Integer(
        string="base_imponible")
    impuestos = fields.Integer(string="impuestos", compute="_impuestos")
    total = fields.Integer(string="total", compute="_total")

    detalle_factura_ids = fields.One2many(
        'contabilidad.detalle', 'factura_id', string='detalles')

    @api.one
    def _impuestos(self):
        self.impuestos = (self.base_imponible * 0.19)

    @api.one
    def _total(self):
        self.total = (self.base_imponible + self.impuestos)
