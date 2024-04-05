from odoo import fields, models, api

class Pathologist(models.Model):
    _name = 'pathologist.activities'
    _rec_name = 'name'
    _description = 'This model describe the Pathologist tasks'

    name = fields.Char(string="Name", required=True)
    id = fields.Integer(string="ID", required=True)
    contact = fields.Char(string="Contact", required=True, default='01xxxxxxxxx')
    address = fields.Text(string="Address", required=True)

    specialization = fields.Selection([
        ('anatomical_pathology', 'Anatomical Pathology'),
        ('clinical_pathology', 'Clinical Pathology'),
        ('surgical_pathology', 'Surgical Pathology'),
        ('hematopathology', 'Hematopathology'),
        ('dermatopathology', 'Dermatopathology'),
        ('neuropathology', 'Neuropathology'),
        ('forensic_pathology', 'Forensic Pathology'),
        ('pediatric_pathology', 'Pediatric Pathology'),
        ('gynecologic_pathology', 'Gynecologic Pathology'),
        ('oncologic_pathology', 'Oncologic Pathology'),

    ], required=True)
    certification = fields.Selection([
        ('board_certified_anatomical_pathologist', 'Board Certified Anatomical Pathologist'),
        ('board_certified_clinical_pathologist', 'Board Certified Clinical Pathologist'),
        ('board_certified_surgical_pathologist', 'Board Certified Surgical Pathologist'),
        ('board_certified_hematopathologist', 'Board Certified Hematopathologist'),
        ('board_certified_dermatopathologist', 'Board Certified Dermatopathologist'),
        ('board_certified_neuropathologist', 'Board Certified Neuropathologist'),
        ('board_certified_forensic_pathologist', 'Board Certified Forensic Pathologist'),
        ('board_certified_pediatric_pathologist', 'Board Certified Pediatric Pathologist'),
        ('board_certified_gynecologic_pathologist', 'Board Certified Gynecologic Pathologist'),
        ('board_certified_oncologic_pathologist', 'Board Certified Oncologic Pathologist')

    ])

    experience = fields.Integer(string="Experience Year")




