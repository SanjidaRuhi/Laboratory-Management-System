from odoo import fields, models

class Appointment(models.Model):
    _name = 'appointment.details'
    _rec_name = 'patient'
    _description = 'This model contains the details of appointment'

    patient = fields.Many2one('patient.details', string='Patient details')
    doctor = fields.Many2one('doctor.details', string='Doctor details')
    email = fields.Char(related='patient.email')
    id = fields.Integer(string="Appointment Id", required=True)
    appointment_date = fields.Date(string="Date of Appointment", required=True)
    appointment_time = fields.Datetime(string="Time", required=True)
