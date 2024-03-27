from odoo import fields, models

class ResUsers(models.Model):

    _inherit = 'res.users'

    property_ids = fields.One2many("estate.property", "buyer", string="Properties", domain=[("status", "in", ["new", "offerr"])])