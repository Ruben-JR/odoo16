# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([("m", "Male"), ("f", "Female")], string="Gender")
