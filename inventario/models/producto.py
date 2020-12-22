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
    precio_venta = fields.Integer(string="Precio Venta", required=True)
    image = fields.Binary(string="Imagen")  # PROBANDO IMAGENES

    # FK ID DEL PROVEEDOR

    proveedor_id = fields.Many2one(
        'inventario.proveedor', string="ID Proveedor")

    # producto_id = fields.Char(string="SKU", unique=True) #ACÁ PODRIA SER EL CODIGO DE BARRA O SKU DE CADA PRODUCTO

    id_detalle_orden_compra = fields.One2many(
        'ventas.detalle_compra', 'producto_ids', string="Producto")

    # producto_id = fields.One2many(
    #     'contabilidad.detalle', 'producto_id', string='producto_id')

    _sql_constraints = [('producto_unique', 'unique(producto_id)',
                         'El SKU no puede coincidir con un producto ya existente en inventario'), ]
