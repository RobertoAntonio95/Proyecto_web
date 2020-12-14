from odoo import models, fields, api


class Factura(models.Model):

    _name = 'contabilidad.factura'
    _description = 'facturas'
    _rec_name = 'fecha_creación'
    # , readonly = True
    vendedor_id = fields.Many2one(
        'contabilidad.vendedor', string='vendedor')
    banco_id = fields.Many2one(
        'contabilidad.banco', string='banco')
    #cliente = fields.Char('Title', required=True)
    fecha_creación = fields.Date("Fecha de creación de la factura")
    fecha_vencimiento = fields.Date("Fecha de vecimiento")
    # base imponible será la suma de todos los valores de los productos
    base_imponible = fields.Monetary(
        string="base_imponible")
    impuestos = fields.Monetary(string="impuestos", compute="_impuestos")
    currency_id = fields.Many2one(
        'res.currency', string="moneda")
    total = fields.Monetary(string="total", compute="_total")
    detalle_factura_ids = fields.One2many(
        'contabilidad.detalle', 'factura_id', string='detalles')
    notas = fields.Text(
        string='notas', default="agregue alguna nota aqui con respecto a esta factura")

    cliente = fields.Many2one('ventas.cliente', string='cliente')

    @api.one
    def _impuestos(self):
        self.impuestos = (self.base_imponible * 0.19)

    @api.one
    def _total(self):
        self.total = (self.base_imponible + self.impuestos)
