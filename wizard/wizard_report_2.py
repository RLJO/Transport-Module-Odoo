'''
Created on Aug 6, 2021

@author: baharali
'''
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError, Warning as UserError


class CMSWizardStudentReport(models.TransientModel):
    _name = 'cms.wizard.bus.report2'
    _description = 'Student Report Wizard'

    from_date = fields.Date('From Date', default=lambda * a: date.today())
    to_date = fields.Date('To Date', default=lambda * a: date.today())
    
    def print_report2(self):
        data = self.read()[0]
        print("------------------------")
        ids = self.env['cms.bus'].search([('date_of_birth','>=',self.from_date),('date_of_birth','<=',self.to_date)]).ids
        return self.env.ref('cms_transport.report_qweb_2_id').report_action(ids, data=data)
