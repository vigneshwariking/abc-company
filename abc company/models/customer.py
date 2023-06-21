from odoo import models, fields


class Customer(models.Model):
    _name = "customer.customer"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    phone_no = fields.Integer(string="Phone_no")
    image = fields.Image(string="Image")
    payment = fields.Integer(string="Payment")
    gender = fields.Selection([('male', 'Male'), ('female', "Female")], 'Gender')
    address = fields.Char(string="Address")

    status = fields.Selection([
        ('active', 'Active'),
        ('in_active', 'In-Active')],
        'Status',
        default='active')
