from odoo import models, fields, api


class Categoria(models.Model):

    _name = 'inventario.categoria'
    _description = 'Categorias asociadas a los productos en bodega'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Char(string="Descripción", required=True)
    
    