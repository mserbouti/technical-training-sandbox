from odoo import models, Command
import logging

_logger = logging.getLogger(__name__)


class Property(models.Model):

    _inherit = "estate.property"

    def change_status_to_sold(self):
        res = super().change_status_to_sold()
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id": prop.buyer.id,
                    "move_type": "out_invoice",
                }
            )
            _logger.info("creation de la commande")
        return res
