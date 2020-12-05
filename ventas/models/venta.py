# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    
    _name = 'ventas.principal'

    name = fields.Char()
    valor = fields.Integer()
    cantidad = fields.Integer()

