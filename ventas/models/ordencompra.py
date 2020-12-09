from odoo import models, fields, api
import time

class ordencompra(models.Model):
    
    _name = 'ventas.ordencompra'
    _description = 'Ordenes de compra'
    _rec_name = 'cliente'
    #_defaults= {'fecha': lambda *a: time.strftime('%Y-%m-%d'),}

    fecha = fields.Date(string="Fecha Actual")

    fecha_limite = fields.Selection([ ('15 dias', '15 dias'),('30 dias', '30 dias'),('10 dias','10 dias')],'Fecha limite', default='10 dias')

    cliente = fields.Many2one('ventas.cliente', string="Cliente")

    total = fields.Many2one(
        'ventas.detalle_orden_compra', string="cantidad total")
    
    impuesto = fields.Integer(string="IVA", required=True)
    validez = fields.Boolean(string="Validez de la compra", required=True)

    #id_vendedor = fields.Many2one()
    #id_cliente = fields.One2many ()

    id_detalle_orden_compra = fields.Many2one(
        'ventas.detalle_orden_compra', string="ID orden de compra")




    