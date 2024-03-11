from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


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
    salesman = fields.Many2one("res.partner", string="Salesman", index=True, default=lambda self: self.env.user)
    buyer = fields.Many2one("res.users", string="Buyer")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total_area", string="Total Area (sqm)")
    best_price = fields.Float(compute="_best_price", string="Best Price")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offer_ids')
    def _best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'))

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_orientation = 0
            self.garden_area = 0
        else:
            self.garden_orientation = 'north'
            self.garden_area = 10
