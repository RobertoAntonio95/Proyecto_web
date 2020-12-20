from odoo import models, fields, api


class Factura(models.Model):

    _name = 'contabilidad.factura'
    _description = 'facturas'
    _rec_name = 'fecha_creación'

    vendedor_id = fields.Many2one(
        'contabilidad.vendedor', string='vendedor')
    banco_id = fields.Many2one(
        'contabilidad.banco', string='banco')
    cliente = fields.Many2one(
        'ventas.cliente', string='cliente')
    currency_id = fields.Many2one(
        'res.currency', string="moneda")

    detalle_factura_ids = fields.One2many(
        'contabilidad.detalle', 'factura_id', string='detalles')

    fecha_creación = fields.Date("Fecha de creación de la factura")
    fecha_vencimiento = fields.Date("Fecha de vecimiento")
    base_imponible = fields.Monetary(string="base_imponible")
    impuestos = fields.Monetary(string="impuestos", compute="_impuestos")
    total = fields.Monetary(string="total", compute="_total")

    notas = fields.Text(
        string='notas', default="agregue alguna nota aqui con respecto a esta factura")

    @api.one
    def _impuestos(self):
        self.impuestos = (self.base_imponible * 0.19)

    @api.one
    def _total(self):
        self.total = (self.base_imponible + self.impuestos)
