from odoo import models, fields, api

class detalle_compra(models.Model):
    _name = 'ventas.detalle_compra'
    _description = 'Detalles de la compra'
    _rec_name = 'producto_ids'



    ordencompra_ids = fields.Many2one('ventas.ordencompra', string="Orden compra ID")
    producto_ids = fields.Many2one('ventas.producto', string="Producto ID")
    
    id_vendedor = fields.Many2one('contabilidad.vendedor', string='Vendedor encargado')
    cantidad = fields.Integer(string="cantidad", required=True, default="1")

   

   
    @api.one
    def _get_precio(self):
        self.precio_total = (self.cantidad * self.producto_ids.preciofinal)
  
    precio_total = fields.Integer(string="total", compute="_get_precio")

    total=fields.Float('TOTAL')

    #producto = fields.One2many('ventas.producto', 'apo_id', string="Listado de productos")
   # producto = fields.Many2one('ventas.producto', string="Listado de productos")
    

   # id_producto = fields.Many2one()

  