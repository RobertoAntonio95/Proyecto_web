from odoo import models, fields, api


class Presupuesto(models.Model):

    _name = 'inventario.presupuesto'
    _description = 'presupuestos'
    _rec_name = 'vendedor_id'


# ACÁ LAS FK QUE UTILIZAREMOS DESDE LAS OTRAS TABLAS

    vendedor_id = fields.Many2one('contabilidad.vendedor', string='ID Vendedor')

    nombre = fields.Many2one('ventas.cliente', string = 'ID Cliente')

    detalle_presupuesto_id = fields.Many2one('inventario.detalle_presupuesto', string = "ID Detalle Presupuesto")

    fecha_creacion = fields.Date(string="Fecha Creación", required=True,  default=fields.date.today())
    fecha_expiracion = fields.Date(string="Fecha Expiración", required=True)
    estado_solicitud = fields.Boolean(string="Estado Solicitud", required=True) 
    impuesto = fields.Boolean(string="IVA", required=True)    
    total = fields.Integer(string="Total", required=True)
    correo = fields.Char(string="Correo electrónico", required=True)
