from odoo import fields, models

class Property(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float(required=True)
    status = fields.Selection(
        copy=False,
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)