from odoo import models, fields, api

class Proveedor(models.Model):

    _name = 'inventario.proveedor'
    _description = 'proveedores'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    marca_representante = fields.Char(string="Marca Representante", required=True)
    telefono = fields.Char(string="Teléfono (Ej: +569AAAABBBB)")
    correo = fields.Char(string="Correo", required=True)
    direccion = fields.Char(string="Dirección", required=True)
    

    #RECORDAR CARGO ...