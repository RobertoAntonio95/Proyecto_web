from odoo import models, fields, api


class Factura(models.Model):

    _name = 'contabilidad.factura'
    _description = 'facturas'

    cliente = fields.Char('Title', required=True)
    fecha_creación = fields.Date("Fecha de creación de la factura")
    fecha_vencimiento = fields.Date("Fecha de vecimiento")
    base_imponible = fields.Integer(string="sin impuestos")
    impuestos = fields.Integer(string="sin impuestos")
    total = fields.Integer(string="sin impuestos")

    vendedor_id = fields.Many2one(
        'contabilidad.vendedor', string='vendedor')

    # detalle_factura_ids = fields.One2many(
    #    'contabilidad.detalle_factura', string='detalles')

# banco_id = fields.Many2one(
#    'contabilidad.banco', string='banco')


class DetalleFactura():

    _name = 'contabilidad.detalle_factura'

    # agrgar id_producto cuando los cabros lo hagan

    cantidad = fields.Integer(string="", default=1)
    precio_unitario = fields.Integer(string="precio")
    sub_total = fields.Integer(string="sub total", compute="_sub_total")
    impuesto = fields.Integer(
        string="impuesto de un 19 porciento", compute="_impuesto")
    total = fields.Integer(
        string="impuesto + total", compute="_total")

    #factura_id = fields.Many2one('contabilidad.factura', string="factura")

    @api.one
    def _sub_total(self):
        self.sub_total = (self.precio_unitario * self.precio_unitario)

    @api.one
    def _impuesto(self):
        self.impuesto = (self.sub_total * 0.19)

    def _total(self):
        self.total = (self.sub_total + self.impuesto)
