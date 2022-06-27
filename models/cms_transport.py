# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date


class CMSChallan(models.Model):
    _name = 'cms.challan'
    _description = 'Challan Information'

    # name = fields.Char('Student Name', required=True)
    fee = fields.Char('Challan Fee', required=True)
    challan_number = fields.Char('Challan Number', required=True)
    challan_details = fields.Many2one('cms.student', 'challan_id')

    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')], 
                             'Status', readonly=True, default="draft")
    
    active = fields.Boolean(default=True)

    def set_done(self):
        '''Method to change state to done'''
        self.state = 'done'

    def set_cancel(self):
        '''Set the state to draft'''
        self.state = 'cancelled'

class CMSRoute(models.Model):
    _name = 'cms.route'
    _description = 'Route Information'

    # name = fields.Char('Student Name', required=True)
    bus_route = fields.Char('Bus Route', required=True)
   
    bus_details = fields.Many2one('cms.bus', 'bus_route')
    

    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')], 
                             'Status', readonly=True, default="draft")
    
    active = fields.Boolean(default=True)

    def set_done(self):
        '''Method to change state to done'''
        self.state = 'done'

    def set_cancel(self):
        '''Set the state to draft'''
        self.state = 'cancelled'

class CMSStudent(models.Model):
    _name = 'cms.student'
    
    _description = 'Student Information'
   
    name = fields.Char('Student Name', required=True)
    father_name = fields.Char('Father Name', required=True)
    
    registration_no = fields.Char(string='Registration No.', required=True)
    bus_no = fields('cms.bus', string='Bus No',required=True)
    cnic = fields.Char(string='Student CNIC')
    contact_phone = fields.Char('Phone no.')

    challan_id = fields.Many2one('cms.challan', 'challan_details')

    grad_date = fields.Integer(compute= '_compute_grad_date', string='Graduation Date', readonly=True)
    admission_date = fields.Date('Admission Date', default=date.today())
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender', states={'done': [('readonly', True)]}, required=True)
    
    user_id = fields.Many2one('res.users', string='Responsible', readonly=True, default=lambda self: self.env.user)
    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer(compute='_compute_student_age', string='Age', readonly=True)
    
    
    
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')], 
                             'Status', readonly=True, default="draft")
    
    active = fields.Boolean(default=True)
    
   
        
    @api.depends('date_of_birth')
    def _compute_student_age(self):
        '''Method to calculate student age'''
        current_date = date.today()
        for rec in self:
            if rec.date_of_birth:
                start = rec.date_of_birth
                age = (current_date - start).days / 365
                # Age should be greater than 0
                if age > 0.0:
                    rec.age = age
                else:
                    rec.age = 0
            else:
                rec.age = 0
    
    @api.depends('admission_date')       
    def _compute_grad_date(self):
        '''Method to calculate expected graduation date'''
        for rec in self:
            if rec.admission_date:
                rec.grad_date = (rec.admission_date).year + 4

    def set_done(self):
        '''Method to change state to done'''
        self.state = 'done'

    def set_cancel(self):
        '''Set the state to draft'''
        self.state = 'cancelled'




    
    
class CMSBus(models.Model):
    _name = 'cms.bus'
    
    _description = 'Bus Register'
   
    bus_number = fields.Char('Bus number', required=True)
    # company_selection = fields.Many2one('account.analytic.account', string="Company")

    registration_no = fields.Char(string='Registration No.', required=True)
   
    pk_name = fields.One2many('cms.student', 'bus_no', string='Students')
    
    bus_route = fields.Many2one('cms.route', 'bus_details')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')], 
                             'Status', readonly=True, default="draft")
    # bus_id = fields.Many2one('cms.student', string="Bus No", related='bus_no.bus_number')
    
    active = fields.Boolean(default=True)
    
    def set_done(self):
        '''Method to change state to done'''
        self.state = 'done'

    def set_cancel(self):
        '''Set the state to draft'''
        self.state = 'cancelled'