# -*- coding: utf-8 -*-
from odoo import http

# class Inventario(http.Controller):
#     @http.route('/inventario/inventario/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventario/inventario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario.listing', {
#             'root': '/inventario/inventario',
#             'objects': http.request.env['inventario.inventario'].search([]),
#         })

#     @http.route('/inventario/inventario/objects/<model("inventario.inventario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario.object', {
#             'object': obj
#         })