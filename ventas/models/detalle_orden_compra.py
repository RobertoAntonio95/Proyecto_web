from odoo import models, fields, api

class detalle_compra(models.Model):
    _name = 'ventas.detalle_compra'
    _description = 'Detalles de la compra'

    id_vendedor = fields.Many2one('contabilidad.vendedor', string='Vendedor encargado')
    id_detalle_orden_compra = fields.Many2one('ventas.detalle_compra', string='Id detalle de compra')   
    cantidad = fields.Char(string="Cantidad de Productos", required=True)

    precio_costo = fields.Many2one('ventas.ordencompra',string="Precio", required=True)

  
    precio_total = fields.Float('Precio Total')

    @api.one
    def _IVA(self):
        self.IVA = self.precio_total * 0.19

    impuestos = fields.Float('IVA', compute=_IVA)

    #producto = fields.One2many('ventas.producto', 'apo_id', string="Listado de productos")
   # producto = fields.Many2one('ventas.producto', string="Listado de productos")
    producto = fields.Many2many('ventas.producto', string = 'Listado de productos')

   # id_producto = fields.Many2one()

  