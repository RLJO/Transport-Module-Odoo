'''
Created on Aug 6, 2021

@author: baharali
'''
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError, Warning as UserError


class CMSWizardStudentReport(models.TransientModel):
    _name = 'cms.wizard.route.report4'
    _description = 'route Report Wizard'

    from_date = fields.Date('From Date', default=lambda * a: date.today())
    to_date = fields.Date('To Date', default=lambda * a: date.today())
    
    def print_report4(self):
        data = self.read()[0]
        print("------------------------")
        ids = self.env['cms.route'].search([('challan_number','>=',self.from_date),('challan_number','<=',self.to_date)]).ids
        return self.env.ref('cms_transport.report_qweb_4_id').report_action(ids, data=data)
