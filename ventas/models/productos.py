
from odoo import models, fields, api

class producto(models.Model):
        _name = 'ventas.producto'
        _description = 'Pagina con Productos'
        
        name = fields.Char()
        valor = fields.Integer()
        cantidad = fields.Integer()
