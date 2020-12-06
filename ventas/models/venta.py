# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    
    _name = 'ventas.principal'

    name = fields.Char(string="Nombre del producto", required=True)
    valor = fields.Integer(string="Valor del producto", required=True)
    cantidad = fields.Integer(string="Cantidad del producto", required=True)
    

