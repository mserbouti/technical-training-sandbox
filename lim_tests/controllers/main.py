from odoo.http import request, route, Controller


class LimTestsController(Controller):
    @route("/essayer-une-selle", type="http", auth="public", website=True)
    def essayer_une_selle(self):
        return request.render("essayer_une_selle", {})
