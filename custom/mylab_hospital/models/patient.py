# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class hospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    ref = fields.Char()
    patient_id = fields.Many2one("res.partner")
    name = fields.Char(related="patient_id.name", tracking=True, required=True)
    date_of_birth = fields.Date(related="patient_id.date_of_birth")
    age = fields.Integer(compute="_calc_age", tracking=True)
    gender = fields.Selection(
        [("m", "Male"), ("f", "Female")],
        tracking=True,
        related="patient_id.gender",
        default="m",
        store=True,
    )
    active = fields.Boolean(default=True)

    @api.depends("date_of_birth")
    def _calc_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = (
                    today.year
                    - rec.date_of_birth.year
                    - (
                        (today.month, today.day)
                        < (rec.date_of_birth.month, rec.date_of_birth.day)
                    )
                )
            else:
                rec.age = 0
