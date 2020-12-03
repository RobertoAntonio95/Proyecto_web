from odoo import models, fields, api


class vendedor(models.Model):

    _name = 'contabilidad.vendedor'
    _description = 'vendedores'

    nombre = fields.Char(string="nombre", required=True)
    rut = fields.Char(string="rut", required=True)
    correo = fields.Char(string="correo", required=True)
    telefono = fields.Integer(string="telefono")
    cargo = fields.Char(string="cargo en la empresa", required=True)
