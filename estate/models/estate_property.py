from dateutil.relativedelta import relativedelta
from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "estate description"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()

    default_date = fields.Datetime.now() + relativedelta(months=3)

    date_availability = fields.Date(string='Available From', copy=False, default=default_date)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('south', 'South'), ('north', 'North'), ('east', 'East'), ('west', 'West')],
        help="Orientation of the garden")
    status = fields.Selection(
        string='Status',
        required=True,
        copy=False,
        selection=[
            ('new', 'New'), 
            ('offerr', 'Offer Received'), 
            ('offerta', 'Offer Accepted'),
            ('soldandc', 'Sold and Canceled')],
        default='new',
        help="Status de l'offre")
    active = fields.Boolean(default=True)
    property_type_id = fields.Many2one("estate.property.type", string="Partner")