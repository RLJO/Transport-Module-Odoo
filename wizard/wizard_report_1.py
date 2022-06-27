'''
Created on Aug 6, 2021

@author: baharali
'''
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError, Warning as UserError


class CMSWizardStudentReport(models.TransientModel):
    _name = 'cms.wizard.student.report1'
    _description = 'Student Report Wizard'

    from_registration_no = fields.Char('From registration_no', required=True)
    to_registration_no = fields.Char('To registration', required=True)
    
    def print_report1(self):
        data = self.read()[0]

        print("------------------------")
        ids = self.env['cms.student'].search([('registration_no','>=',self.from_registration_no),('registration_no','<=',self.to_registration_no)]).ids
       
        return self.env.ref('cms_transport.report_qweb_1_id').report_action(ids, data=data)