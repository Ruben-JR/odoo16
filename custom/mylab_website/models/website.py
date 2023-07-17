# -*- coding: utf-8 -*-

from odoo import models, fields, api


class website(models.Model):
    _inherit = "res.partner"

    patient_name = fields.Char(string="Patient name")
    date_of_birth = fields.Date(string="date of bithday")
    gender = fields.Selection(
        [("m", "Male"), ("f", "Female")], tracking=True, default="m"
    )
    is_patient = fields.Boolean(default=True)
