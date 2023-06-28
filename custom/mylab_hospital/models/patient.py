# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    ref = fields.Char(readonly=True)
    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([("m", "Male"), ("f", "Female")])
    active = fields.Boolean(default=True)
