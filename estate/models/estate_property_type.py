from odoo import api, fields, models


class Property(models.Model):
    _name = "estate.property.type"
    _description = "estate property type"
    _order = "name asc"

    name = fields.Char(required=True)
    property_ids = fields.One2many(
        "estate.property", "property_type_id", string="Properties"
    )
    sequence = fields.Integer(string="Sequence")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_count_offer_ids")

    @api.depends("offer_ids")
    def _count_offer_ids(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
