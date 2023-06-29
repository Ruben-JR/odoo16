# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    patient_id = fields.Many2one("hospital.patient")
    appoint_time = fields.Datetime()
    book_date = fields.Date()
