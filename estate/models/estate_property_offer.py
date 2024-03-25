from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class Property(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"
    _order = "price desc"

    price = fields.Float(required=True)
    status = fields.Selection(
        copy=False,
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("res.users", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", string="Date Deadline")
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id")

    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)',
         'Offer Price must be positive.')
    ]

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    @api.depends("validity", "create_date")
    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def offer_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("An offer as already been accepted.")
        self.write(
            {
                "status": "accepted",
            }
        )
        return self.mapped("property_id").write(
            {
                "selling_price": self.price,
                "buyer": self.partner_id.id,
            }
        )

    def offer_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
