from odoo import fields, models

class Patient(models.Model):
    _name = 'patient.details'
    #_inherit = ['mail..thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _description = 'This model contains the details of the patients'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    id = fields.Integer(string="ID", required=True)
    color = fields.Integer(string="color picker")
    color_two = fields.Char(string="color")
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
    #doctor_id = fields.Many2one('res.user', string='Doctor')
    doctor = fields.Many2many('doctor.details', string='Doctor')
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

    email = fields.Char(string="Email", help="provide your email according to the syntex", required=True, default='someone@gmail.com')
    contact = fields.Char(string="Contact", required=True, default='01xxxxxxxxx')
    address = fields.Text(string="Address", required=True)
    active = fields.Boolean(string="Active", default=True)
    image = fields.Image(string="Profile Picture")

    def object_button(self):
        print("object Button Clicked")
        return {
            'effect': {
                'fedout': 'slow',
                'message': 'object button clicked!!!!',
                'type': 'rainbow_man',


            }
        }
