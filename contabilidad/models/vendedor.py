from odoo import models, fields, api


class Cargo(models.Model):

    _name = 'contabilidad.cargo'
    _description = 'cargo de vendedores'
    _rec_name = 'nombre'

    vendedor_ids = fields.One2many(
        'contabilidad.vendedor',
        'cargo_id',
        string='numero de personas x cargo'
    )

    cont_trabajadores = fields.Integer(compute='_cont_workers')
    nombre = fields.Char(string="nombre", required=True)

    @api.one
    def _cont_workers(self):
        self.cont_trabajadores = len(self.vendedor_ids)


class Vendedor(models.Model):

    _name = 'contabilidad.vendedor'
    _description = 'vendedores'
    _rec_name = 'nombre'

    nombre = fields.Char(string="nombre", required=True)
    rut = fields.Char(string="rut", required=True)
    correo = fields.Char(string="correo", required=True)
    telefono = fields.Integer(string="telefono")

    cargo_id = fields.Many2one(
        'contabilidad.cargo', string='cargo en la empresa')

    facturas_ids = fields.One2many(
        'contabilidad.factura',
        'vendedor_id',
        string='numero de facturas x vendedor'
    )
    cont_facturas = fields.Integer(compute='_cont_facturas')

    @api.one
    def _cont_facturas(self):
        self.cont_facturas = len(self.facturas_ids)
