# -*- coding: utf-8 -*-
# from odoo import http


# class Uposports(http.Controller):
#     @http.route('/uposports/uposports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uposports/uposports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uposports.listing', {
#             'root': '/uposports/uposports',
#             'objects': http.request.env['uposports.uposports'].search([]),
#         })

#     @http.route('/uposports/uposports/objects/<model("uposports.uposports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uposports.object', {
#             'object': obj
#         })
