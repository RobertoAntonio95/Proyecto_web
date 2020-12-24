from odoo import models, fields, api

class cliente(models.Model):
    
    _name = 'ventas.cliente'
    _description = 'Clientes de la empresa'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    rut = fields.Char(string="RUT", required=True)
    correo = fields.Char(string="Correo", required=True)
    banco_id = fields.Many2one('contabilidad.banco',string="Banco")
    telefono = fields.Char(string="Telefono", required=True)    

 