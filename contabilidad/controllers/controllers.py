# -*- coding: utf-8 -*-
from odoo import http

# class Contabilidad(http.Controller):
#     @http.route('/contabilidad/contabilidad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contabilidad/contabilidad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contabilidad.listing', {
#             'root': '/contabilidad/contabilidad',
#             'objects': http.request.env['contabilidad.contabilidad'].search([]),
#         })

#     @http.route('/contabilidad/contabilidad/objects/<model("contabilidad.contabilidad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contabilidad.object', {
#             'object': obj
#         })