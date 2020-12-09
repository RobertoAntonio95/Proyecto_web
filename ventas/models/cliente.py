from odoo import models, fields, api

class cliente(models.Model):
    
    _name = 'ventas.cliente'
    _description = 'Clientes de la empresa'

    nombre = fields.Char(string="Nombre", required=True)
    rut = fields.Char(string="RUT", required=True)
    correo = fields.Char(string="Correo", required=True)
    empresa = fields.Char(string="Empresas", required=True)
    telefono = fields.Char(string="Telefono", required=True)    

    cliente_id = fields.Many2one(
          'ventas.ordencompra', string='Codigo del cliente')