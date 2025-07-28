from odoo.http import request, route, Controller


class LimTestsController(Controller):
    @route("/try-saddle", auth="public")
    def hello(self):
        return request.render(
            "limtests.hello"
            # ,
            # {
            #     "session_info": request.env["ir.http"].get_frontend_session_info(),
            # },
        )
