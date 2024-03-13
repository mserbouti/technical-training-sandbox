from datetime import timedelta

from odoo import api, fields, models


class Property(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float(required=True)
    status = fields.Selection(
        copy=False,
        string='Status',
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("res.users", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", string="Date Deadline")

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
        for record in self:
            record.status = 'accepted'
        return True

    def offer_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
