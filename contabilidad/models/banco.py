from odoo import models, fields, api


class Banco(models.Model):

    _name = 'contabilidad.banco'
    _description = 'bancos donde se reciben pagos'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)
