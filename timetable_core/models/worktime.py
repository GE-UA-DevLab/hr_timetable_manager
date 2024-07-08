# -*- coding: utf-8 -*-

from odoo import fields, models


class Worktime(models.Model):
    _name = 'timetable.worktime'
    _description = 'Timetable Worktime'

    employee_id = fields.Many2one(comodel_name='hr.employee')
    period = fields.Date()
    d1 = fields.Float(string="1")
    d2 = fields.Float(string="2")
    d3 = fields.Float(string="3")
    d4 = fields.Float(string="4")
    d5 = fields.Float(string="5")
    d6 = fields.Float(string="6")
    d7 = fields.Float(string="7")
    d8 = fields.Float(string="8")
    d9 = fields.Float(string="9")
    d10 = fields.Float(string="10")
    d11 = fields.Float(string="11")
    d12 = fields.Float(string="12")
    d13 = fields.Float(string="13")
    d14 = fields.Float(string="14")
    d15 = fields.Float(string="15")
    d16 = fields.Float(string="16")
    d17 = fields.Float(string="17")
    d18 = fields.Float(string="18")
    d19 = fields.Float(string="19")
    d20 = fields.Float(string="20")
    d21 = fields.Float(string="21")
    d22 = fields.Float(string="22")
    d23 = fields.Float(string="23")
    d24 = fields.Float(string="24")
    d25 = fields.Float(string="25")
    d26 = fields.Float(string="26")
    d27 = fields.Float(string="27")
    d28 = fields.Float(string="28")
    d29 = fields.Float(string="29")
    d30 = fields.Float(string="30")
    d31 = fields.Float(string="31")
