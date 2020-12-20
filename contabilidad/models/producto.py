from odoo import models, fields, api


class Producto(models.Model):

    _name = 'contabilidad.producto'
    _description = 'productos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre pruducto", required=True)
    detalle = fields.Char(string="detalle")
    precio = fields.Integer(string="precio")

    detalle_ids = fields.One2many(
        'contabilidad.detalle', 'producto_id', string='detalle productos')
