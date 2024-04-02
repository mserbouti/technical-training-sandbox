from odoo import fields, models


class Property(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag"
    _order = "name asc"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color")

    _sql_constraints = [
        ("unique_tag_name", "UNIQUE(name)", "Le nom du tag doit être unique.")
    ]
