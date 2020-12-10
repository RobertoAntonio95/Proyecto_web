from odoo import models, fields, api


class inventario(models.Model):

    _name = 'inventario.presupuesto'
    _description = 'presupuestos'
    _rec_name = 'fecha_creación'

# ACÁ LAS FK QUE UTILIZAREMOS DESDE LAS OTRAS TABLAS

    vendedor_id = fields.Many2one(
        'contabilidad.vendedor', string='vendedor')

    cliente_id = fields.Many2one(     #PRUEBA DE LINEA DE CODIGO
        'ventas.cliente', string = 'cliente')

    detalle_presupuesto_id = fields.Many2one(   #FALTA CREAR DETALLE PRESP.
        
    )

    fecha = fields.Char(string="fecha", required=True)
    fecha_limite = fields.Char(string="fecha_limite", required=True)
    total = fields.Integer(string="total", required=True)
    estado_solicitud = fields.Boolean(Boolean="estado_solicitud", required=True) #DUDA MAYUSCULA
    impuesto = fields.float(string="impuesto", required=True)    # PENSANDO QUE NO FUERA UN VALOR ENTERO
    total = fields.Integer(string="total", required=True)
    correo = fields.Char(string="correo", required=True)
