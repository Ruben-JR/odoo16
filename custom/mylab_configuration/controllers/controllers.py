# -*- coding: utf-8 -*-
# from odoo import http


# class MylabConfiguration(http.Controller):
#     @http.route('/mylab_configuration/mylab_configuration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mylab_configuration/mylab_configuration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mylab_configuration.listing', {
#             'root': '/mylab_configuration/mylab_configuration',
#             'objects': http.request.env['mylab_configuration.mylab_configuration'].search([]),
#         })

#     @http.route('/mylab_configuration/mylab_configuration/objects/<model("mylab_configuration.mylab_configuration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mylab_configuration.object', {
#             'object': obj
#         })
