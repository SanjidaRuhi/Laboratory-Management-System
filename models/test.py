from odoo import fields, models, api

class Test(models.Model):
    _name = 'test.details'
    _rec_name = 'test_name'
    _description = 'This model describe the descriptions of the test'

    test_name = fields.Char(string="Test Name", required=True)
    test_id = fields.Integer(string="Test ID", required=True)
    cost = fields.Integer(string="Cost", required=True)
    description = fields.Text(string='Description')
    preparation = fields.Text(string='Preparation')
    testCategory = fields.Selection([
        ('chemistry', 'Chemistry'),
        ('hematology', 'Hematology'),
        ('microbiology', 'Microbiology'),
        ('immunology', 'Immunology'),
        ('serology', 'Serology'),
        ('molecular diagnostics', 'Molecular Diagnostics'),
        ('histopathology', 'Histopathology'),
        ('urinalysis', 'Urinalysis'),
        ('radiology', 'Radiology'),
        ('toxicology', 'Toxicology'),

    ], required=True)
    units = fields.Text(string='Units')

    start_date = fields.Date(string='Start date', default= fields.Date.context_today)
    end_date_time = fields.Datetime(string='End date time', default= fields.Datetime.now)
    html_field = fields.Html(string = 'HTML Field')
    pathologist = fields.Many2one('pathologist.activities', string='Pathologist')








