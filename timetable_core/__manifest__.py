# -*- coding: utf-8 -*-
{
    'name': "HR Timetables",

    'author': "Anton Berh",
    'website': "https://github.com/antonbergit",

    'category': 'Human Resources',
    'version': '17.0.0.0.1',
    'license': 'LGPL-3',
    'depends': ['hr'],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee.xml',
        'views/schedule.xml',
        'data/defaults_schedule.xml',
    ],
}
