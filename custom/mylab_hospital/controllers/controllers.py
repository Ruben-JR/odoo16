# -*- coding: utf-8 -*-
# from odoo import http


# class MylabHospital(http.Controller):
#     @http.route('/mylab_hospital/mylab_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mylab_hospital/mylab_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mylab_hospital.listing', {
#             'root': '/mylab_hospital/mylab_hospital',
#             'objects': http.request.env['mylab_hospital.mylab_hospital'].search([]),
#         })

#     @http.route('/mylab_hospital/mylab_hospital/objects/<model("mylab_hospital.mylab_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mylab_hospital.object', {
#             'object': obj
#         })
