from odoo import models, fields, api

class Proveedor(models.Model):

    _name = 'inventario.proveedor'
    _description = 'proveedores'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)
    marca_representante = fields.Char(string="marca representante", required=True)
    telefono = fields.Integer(string="telefono")
    correo = fields.Char(string="correo", required=True)
    direccion = fields.Char(string="direccion", required=True)
    

    #CARGO