from odoo import _, models, fields


class Member(models.Model):
    _name = "member.member"

    name = fields.Char(string="Name")
    phone_number = fields.Integer(string="phone_number")
    user_email = fields.Char(string="User Email")
    address = fields.Char(string="Address")
    age = fields.Integer(string="age")
    user_id = fields.Integer(string="user_id")
    date_of_birth = fields.Date(string="Date_of_birth")
    image = fields.Image(string="Image")
    payment = fields.Integer(string='Payment')

    customer_ids = fields.One2many('member.details', 'member_ids', string='Member')


class MemberDetails(models.Model):
    _name = 'member.details'

    member_ids = fields.Many2one('member.member', string='Member')
