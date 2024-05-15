from odoo.http import request, route, Controller


class EstateController(Controller):
    @route("/estate/hello", auth="public")
    def hello(self):
        return request.render(
            "estate.hello",
            {
                "session_info": request.env["ir.http"].get_frontend_session_info(),
            },
        )
