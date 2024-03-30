from odoo import fields, models

class Patient(models.Model):
    _name = 'patient.details'
    _rec_name = 'name'
    _description = 'This model contains the details of the patients'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    id = fields.Integer(string="ID", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True)
    priority = fields.Selection([
        ('1', 'Normal'),
        ('2', 'Emergency'),
        ('3', 'Critical'),
        ('4', 'Very Critical'),

    ])
    status = fields.Selection([
        ('appointed', 'Appointed'),
        ('checkup', 'Checkup'),
        ('on_test', 'On Test'),
        ('emergency', 'Emergency'),
        ('admitted', 'Admitted'),
        ('ot', 'OT'),
        ('icu', 'ICU'),
        ('released', 'Released'),

    ], default='appointed', required=True)

    email = fields.Char(string="Email", required=True, default='someone@gmail.com')
    contact = fields.Char(string="Contact", required=True, default='01xxxxxxxxx')
    address = fields.Text(string="Address", required=True)
    appointment = fields.Many2one('appointment.details', string='Appointment details')






