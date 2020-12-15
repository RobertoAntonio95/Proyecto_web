from odoo import models, fields, api


class Presupuesto(models.Model):

    _name = 'inventario.presupuesto'
    _description = 'presupuestos'


# ACÁ LAS FK QUE UTILIZAREMOS DESDE LAS OTRAS TABLAS

   # vendedor_id = fields.Many2one(
   #     'contabilidad.vendedor', string='vendedor')

   # cliente_id = fields.Many2one(     #PRUEBA DE LINEA DE CODIGO
   #     'ventas.cliente', string = 'cliente')

   # detalle_presupuesto_id = fields.Many2one(   #FALTA CREAR DETALLE PRESP.     
   # )

    fecha = fields.Date(string="Fecha")
    fecha_limite = fields.Date(string="fecha_limite", required=True)
    total = fields.Integer(string="Total", required=True)
    estado_solicitud = fields.Boolean(string="Estado_solicitud", required=True) #DUDA MAYUSCULA
    impuesto = fields.Float(string="Impuesto", required=True)    # PENSANDO QUE NO FUERA UN VALOR ENTERO
    total = fields.Integer(string="Total", required=True)
    correo = fields.Char(string="Correo electrónico", required=True)
