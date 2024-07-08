# -*- coding: utf-8 -*-

from odoo import fields, models


class Employee(models.Model):
    _inherit = "hr.employee"

    schedule_id = fields.Many2one(
        comodel_name='timetable.schedule',
        string='Schedule',)
    worktime_ids = fields.One2many(
        comodel_name='timetable.worktime',
        inverse_name='employee_id',)
