/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Layout } from "@web/search/layout";
import { useService } from "@web/core/utils/hooks";
import { DashboardItem } from "./dashboard_item/dashboard_item";

class AwesomeDashboard extends Component {
  static template = "awesome_dashboard.AwesomeDashboard";
  static components = { Layout, DashboardItem };

  setup() {
    this.display = {
      controlPanel: {},
    };
    this.action = useService("action");
    this.statistics = useState(useService("awesome_dashboard.statistics"));
    this.items = registry.category("awesome_dashboard").getAll();
  }

  openCustomers() {
    this.action.doAction("base.action_partner_form");
  }

  openLeads() {
    this.action.doAction({
      type: "ir.actions.act_window",
      name: "Leads",
      res_model: "crm.lead",
      views: [
        [false, "list"],
        [false, "form"],
      ],
    });
  }
}
registry.category("lazy_components").add("AwesomeDashboard", AwesomeDashboard);
