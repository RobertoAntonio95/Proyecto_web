from odoo import models, fields, api


class Detalle(models.Model):

    _name = 'contabilidad.detalle'
    _description = 'detalles de facturas'
    _rec_name = 'factura_id'

    factura_id = fields.Many2one('contabilidad.factura', string="factura_id")

    # ----------- ID A PRODUCTO -------------
    producto_id = fields.Many2one(
        'inventario.producto', string="producto_id")

    nombre = fields.Char(string="Nombre producto",
                         readonly="1", compute="_get_nombre")
    cantidad = fields.Integer(string="Cantidad", required=True, default="1")
    precio_venta = fields.Integer(
        string="precio unidad", readonly="1", compute="_get_precio_venta")
    total = fields.Integer(string="Precio total", compute="_get_precio")
    marca = fields.Char(string="marca", readonly="1", compute="_get_marca")

    @api.one
    def _get_precio(self):
        self.total = (self.cantidad * self.producto_id.precio_venta)

    @api.one
    def _get_nombre(self):
        self.nombre = self.producto_id.nombre

    @api.one
    def _get_marca(self):
        self.marca = self.producto_id.marca

    @api.one
    def _get_precio_venta(self):
        self.precio_venta = self.producto_id.precio_venta

    @api.onchange('producto_id')
    def _onchange(self):
        self.total = self.producto_id.precio_venta
        self.nombre = self.producto_id.nombre
        self.marca = self.producto_id.marca
        self.precio_venta = self.producto_id.precio_venta
