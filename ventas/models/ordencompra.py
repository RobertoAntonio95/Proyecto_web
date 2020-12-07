from odoo import models, fields, api

class ordencompra(models.Model):
    
    _name = 'ventas.ordencompra'
    _description = 'Ordenes de compra'

    fecha = fields.Char(string="Fecha de compra", required=True)
    fecha_limite = fields.Char(string="Fecha limite", required=True)
    total = fields.Integer(string="Cantidad del producto", required=True)
    impuesto = fields.Integer(string="Valor Total", required=True)
    validez = fields.Boolean(string="Validez de la compra", required=True)

    #id_vendedor = fields.Many2one()
    #id_cliente = fields.One2many ()

    id_detalle_orden_compra = fields.Many2one(
        'ventas.ordencompra', string="ID orden de compra")
    