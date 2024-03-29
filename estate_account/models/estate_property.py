from odoo import models, Command
import logging

_logger = logging.getLogger(__name__)


class Property(models.Model):

    _inherit = "estate.property"

    def change_status_to_sold(self):
        res = super().change_status_to_sold()
        for prop in self:
            invoice_vals = {
                    "partner_id": prop.buyer.id,
                    "move_type": "out_invoice",
                    "line_ids": [
                        Command.create({
                            "name": prop.name,
                            "quantity": 1,
                            "price_unit": prop.selling_price * 0.06,
                        }),
                        Command.create({
                            "name": "administrative fees",
                            "quantity": 1,
                            "price_unit": 100,
                        })
                    ],
                }
            invoice = prop.env["account.move"].create(invoice_vals)
            invoice.action_post() # sans ça le commande va passer dans draft
            _logger.info("creation de la commande")
        return res
