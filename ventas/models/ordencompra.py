from odoo import models, fields, api

class ordencompra(models.Model):
    
    _name = 'ventas.ordencompra'
    _description = 'Ordenes de compra'
    _rec_name = 'cliente'
  

    cliente = fields.Many2one('ventas.cliente', string="Cliente")

    fecha = fields.Date(string="Fecha Actual", required=True, default=fields.date.today())

    fecha_limite = fields.Selection([ ('15 dias', '15 dias'),
    ('30 dias', '30 dias'),('10 dias','10 dias')],'Fecha limite', default='10 dias', required=True)

    metodo_pago = fields.Selection([ ('Credito', 'Credito'),
    ('Debito', 'Debito'),('Cheques','Cheques'), ('Efectivo','Efectivo')],'Metodo de pago', default='Efectivo') 
    
    orden_compra_ids= fields.One2many('ventas.detalle_compra', 'ordencompra_id', string ="Detalle")
    


    



    