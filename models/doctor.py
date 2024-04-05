from odoo import fields, models, api

class Doctor(models.Model):
    _name = 'doctor.details'
    _rec_name = 'name'
    _description = 'This model describe about doctor'

    name = fields.Char(string="Name", required=True)
    id = fields.Integer(string="ID", required=True)
    license_id = fields.Integer(string="License ID", required=True)
    contact = fields.Char(string="Contact", required=True, default='01xxxxxxxxx')
    clinic_location = fields.Text(string="Clinic Location", required=True)
    active_days = fields.Char(string="Active days", required=True)

    specialization = fields.Selection([
        ('internal_medicine', 'Internal Medicine'),
        ('family_medicine', 'Family Medicine'),
        ('pediatrics', 'Pediatrics'),
        ('obstetrics_gynecology', 'Obstetrics & Gynecology'),
        ('psychiatry', 'Psychiatry'),
        ('surgery', 'Surgery'),
        ('orthopedics', 'Orthopedics'),
        ('urology', 'Urology'),
        ('ophthalmology', 'Ophthalmology'),
        ('otolaryngology', 'Otolaryngology')

    ], required=True)
    certification = fields.Selection([
        ('MD', 'Doctor of Medicine'),
        ('DO', 'Doctor of Osteopathic Medicine'),
        ('MBBS', 'Bachelor of Medicine, Bachelor of Surgery'),
        ('FRCP', 'Fellow of the Royal College of Physicians'),
        ('FRCS', 'Fellow of the Royal College of Surgeons'),
        ('FACP', 'Fellow of the American College of Physicians'),
        ('FACOG', 'Fellow of the American College of Obstetricians and Gynecologists'),
        ('FACS', 'Fellow of the American College of Surgeons'),
        ('FCCP', 'Fellow of the American College of Chest Physicians'),
        ('FCAP', 'Fellow of the College of American Pathologists'),
        ('PHD', 'Doctor of Philosophy'),

    ])

    experience = fields.Integer(string="Experience Year")
    consultation_fee = fields.Float(string="Consultation Fee")




