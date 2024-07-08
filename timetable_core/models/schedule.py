# -*- coding: utf-8 -*-

from odoo import fields, models

schedule_mark = [
    ('D', 'D'),
    ('W', 'W'),
]


class Schedule(models.Model):
    _name = 'timetable.schedule'
    _description = 'Timetable Schedule'

    name = fields.Char()
    d1 = fields.Selection(selection=schedule_mark, string="1")
    d2 = fields.Selection(selection=schedule_mark, string="2")
    d3 = fields.Selection(selection=schedule_mark, string="3")
    d4 = fields.Selection(selection=schedule_mark, string="4")
    d5 = fields.Selection(selection=schedule_mark, string="5")
    d6 = fields.Selection(selection=schedule_mark, string="6")
    d7 = fields.Selection(selection=schedule_mark, string="7")
    d8 = fields.Selection(selection=schedule_mark, string="8")
    d9 = fields.Selection(selection=schedule_mark, string="9")
    d10 = fields.Selection(selection=schedule_mark, string="10")
    d11 = fields.Selection(selection=schedule_mark, string="11")
    d12 = fields.Selection(selection=schedule_mark, string="12")
    d13 = fields.Selection(selection=schedule_mark, string="13")
    d14 = fields.Selection(selection=schedule_mark, string="14")
    d15 = fields.Selection(selection=schedule_mark, string="15")
    d16 = fields.Selection(selection=schedule_mark, string="16")
    d17 = fields.Selection(selection=schedule_mark, string="17")
    d18 = fields.Selection(selection=schedule_mark, string="18")
    d19 = fields.Selection(selection=schedule_mark, string="19")
    d20 = fields.Selection(selection=schedule_mark, string="20")
    d21 = fields.Selection(selection=schedule_mark, string="21")
    d22 = fields.Selection(selection=schedule_mark, string="22")
    d23 = fields.Selection(selection=schedule_mark, string="23")
    d24 = fields.Selection(selection=schedule_mark, string="24")
    d25 = fields.Selection(selection=schedule_mark, string="25")
    d26 = fields.Selection(selection=schedule_mark, string="26")
    d27 = fields.Selection(selection=schedule_mark, string="27")
    d28 = fields.Selection(selection=schedule_mark, string="28")
    d29 = fields.Selection(selection=schedule_mark, string="29")
    d30 = fields.Selection(selection=schedule_mark, string="30")
    d31 = fields.Selection(selection=schedule_mark, string="31")
