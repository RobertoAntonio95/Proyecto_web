from odoo import models, fields, api

class ordencompra(models.Model):
    
    _name = 'ventas.ordencompra'
    _description = 'Ordenes de compra'

    fecha = fields.Date(string="Fecha Actual")
    fecha_limite = fields.Char(string="Fecha limite", required=True)

    total = fields.Many2one('ventas.detalle_orden_compra', string="cantidad total")
    
    impuesto = fields.Integer(string="IVA", required=True)
    validez = fields.Boolean(string="Validez de la compra", required=True)

    #id_vendedor = fields.Many2one()
    #id_cliente = fields.One2many ()

    id_detalle_orden_compra = fields.Many2one(
        'ventas.detalle_orden_compra', string="ID orden de compra")
    

    