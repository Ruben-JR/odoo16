# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one("hospital.patient")
    ref = fields.Char(readonly=True, related="patient_id.ref")
    gender = fields.Selection(related="patient_id.gender")
    appoint_time = fields.Datetime(default=fields.Datetime.now)
    book_date = fields.Date(default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection(
        [("0", "Very Low"), ("1", "Low"), ("2", "Normal"), ("3", "High")],
        string="Priority",
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_cusultation", "In Consultation"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
        string="Status",
        required=True,
    )

    @api.onchange("patient_id")
    def _onchange_patient_id(self):
        for rec in self:
            rec.ref = rec.patient_id.ref

    def object_button(self):
        print("")
