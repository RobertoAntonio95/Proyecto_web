from odoo import models, fields, api


class Cargo(models.Model):

    _name = 'contabilidad.cargo'
    _description = 'cargo de vendedores'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)


class Vendedor(models.Model):

    _name = 'contabilidad.vendedor'
    _description = 'vendedores'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)
    rut = fields.Char(string="rut", required=True)
    correo = fields.Char(string="correo", required=True)
    telefono = fields.Integer(string="telefono")

    cargo_id = fields.Many2one(
        'contabilidad.cargo', string='cargo en la empresa')
