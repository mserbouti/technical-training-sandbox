from odoo import fields, models

class Property(models.Model):
    _name = "estate.property.type"
    _description = "estate property type"
    _order = "name asc"

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer(string="Sequence")
    