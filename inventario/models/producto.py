from odoo import models, fields, api


class Producto(models.Model):

    _name = 'inventario.producto'
    _description = 'productos'
    
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    marca = fields.Char(string="Marca", required=True)
    stock = fields.Integer(string="Stock", required=True)
    stock_critico = fields.Integer(string="Stock Crítico", required=True)
    impuesto = fields.Boolean(string="IVA", required=True)
    precio_costo = fields.Integer(string="Precio Costo", required=True)
    precio_final = fields.Integer(string="Precio Final", required=True)
   # imagen = fields.Binary(string="Imagen") #PROBANDO IMAGENES

    # FK ID DEL PROVEEDOR

    proveedor_id = fields.Many2one(
        'inventario.proveedor', string="ID Proveedor")
    
    producto_id = fields.Integer(string="SKU", unique=True) #ACÁ PODRIA SER EL CODIGO DE BARRA O SKU DE CADA PRODUCTO


    _sql_constraints = [   ('producto_unique', 'unique(producto_id)', 'El SKU no puede coincidir con un producto ya existente en inventario'), ]   