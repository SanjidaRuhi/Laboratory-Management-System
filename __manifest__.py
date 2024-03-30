# -*- coding: utf-8 -*-
{
    'name': "laboratory_management_system",

    'summary': """
        this is a laboratory management system """,

    'description': """
        This is central lab. It has three branches......
    """,
    'sequence' : '-100',

    'author': "S. A. Ru.",

    'website': "",

    'category': 'Medical',

    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/appointment_views.xml',
        'views/doctor_views.xml',
    ],

}