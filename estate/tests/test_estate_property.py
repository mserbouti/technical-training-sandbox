from dateutil.relativedelta import relativedelta

from odoo import fields
from odoo.exceptions import UserError  # type: ignore
from odoo.tests.common import TransactionCase  # type: ignore

# to start test add : --test-enable


class TestProperty(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProperty, self).setUp()

        self.prop_record_01 = self.env["estate.property"].create(
            {
                "name": "Test Property",
                "description": "This is a test property",
                "postcode": "12345",
                "expected_price": 100000,
                "bedrooms": 3,
                "living_area": 150,
                "facades": 2,
                "garage": True,
                "garden": True,
                "garden_area": 50,
                "garden_orientation": "south",
                "status": "new",
                "active": True,
            }
        )

    def test_01_property_values(self):
        property_id = self.prop_record_01

        self.assertRecordValues(
            property_id,
            expected_values=[
                {
                    "name": "Test Property",
                    "description": "This is a test property",
                    "postcode": "12345",
                    "expected_price": 100000,
                    "bedrooms": 3,
                    "living_area": 150,
                    "facades": 2,
                    "garage": True,
                    "garden": True,
                    "garden_area": 50,
                    "garden_orientation": "south",
                    "status": "new",
                    "active": True,
                }
            ],
        )
