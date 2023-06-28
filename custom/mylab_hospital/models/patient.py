# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    ref = fields.Char(readonly=True)
    name = fields.Char(tracking=True, required=True)
    age = fields.Integer(tracking=True)
    gender = fields.Selection([("m", "Male"), ("f", "Female")], tracking=True)
    active = fields.Boolean(default=True)
