from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_utils


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
            ('sold', 'Sold'),
            ('canceled', 'Canceled')],
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

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'Expected Price must be positive.'),
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'Selling Price must be positive.')
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offer_ids')
    def _best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_orientation = 'north'
            self.garden_area = 10
        else:
            self.garden_orientation = 0
            self.garden_area = 0


    @api.depends('selling_price')
    def _selling_price(self):
        for record in self:
            accepted_offers = record.offer_ids.filtered(lambda offer: offer.status == 'accepted')
            if accepted_offers:
                max_price_offer = max(accepted_offers, key=lambda offer: offer.price)
                record.selling_price = max_price_offer.price
                record.buyer = max_price_offer.partner_id
            else:
                record.selling_price = 0.0

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < 10:
                raise UserError('grand')

    def change_status_to_canceled(self):
        for record in self:
            if record.status != 'sold':
                record.status = 'canceled'
            else:
                raise UserError(('is sold !!'))
        return True

    def change_status_to_sold(self):
        for record in self:
            if record.status != 'canceled':
                record.status = 'sold'
            else:
                raise UserError(('is canceled !!'))
        return True
