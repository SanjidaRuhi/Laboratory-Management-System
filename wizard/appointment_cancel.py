from odoo import fields, models

class Patient(models.TransientModel):
    _name = 'appointment.cancel'
    _description = 'This is a Transient model'

    appointment_ids = fields.Many2many("appointment.details", string="Appointment ID", required=True)
    reason = fields.Text(string="Reason")

    def cancel_action(self):
        print("Appointment Cancel")
        return