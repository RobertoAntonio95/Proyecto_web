# -*- coding: utf-8 -*-
from odoo import http

# class Ventas(http.Controller):
#     @http.route('/ventas/ventas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ventas/ventas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ventas.listing', {
#             'root': '/ventas/ventas',
#             'objects': http.request.env['ventas.ventas'].search([]),
#         })

#     @http.route('/ventas/ventas/objects/<model("ventas.ventas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ventas.object', {
#             'object': obj
#         })