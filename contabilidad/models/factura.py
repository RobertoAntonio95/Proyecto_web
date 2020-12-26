from odoo import models, fields, api
from datetime import datetime


class Factura(models.Model):

    _name = 'contabilidad.factura'
    _description = 'facturas'
    _rec_name = 'fecha_creación'

    vendedor_id = fields.Many2one(
        'contabilidad.vendedor', string='vendedor')
    banco_id = fields.Many2one(
        'contabilidad.banco', string='banco')
#    cliente = fields.Text(string='cliente', default='cliente')
    cliente = fields.Many2one(
        'ventas.cliente', string='cliente')
    currency_id = fields.Many2one(
        'res.currency', string="moneda")

    detalle_factura_ids = fields.One2many(
        'contabilidad.detalle', 'factura_id', string='detalles')

    fecha_creación = fields.Date(
        String="Fecha de creación de la factura", default=fields.Date.today())

    fecha_vencimiento = fields.Date("Fecha de vecimiento")
    base_imponible = fields.Integer(
        string="base_imponible", compute="_calcularla"
    )
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

    @api.one
    def _calcularla(self):
        compras = self.env['contabilidad.detalle'].search(
            [('factura_id', '=', self.id)])
        total_compra = 0
        for i in compras:
            total_compra += i.total
        self.base_imponible = total_compra

    #      num = 0
#
    #      # esta funciona a medias
    #      # for total in self.detalle_factura_ids:
    #      #     num += int(total)
    #      # self.base_imponible = (self.base_imponible + num)
#
    #      # for detalle in self.detalle_factura_ids:
    #      #     for total in self.detalle_factura_ids.total:
    #      #         num += 1
    #      # self.base_imponible = (self.base_imponible + num)
#
