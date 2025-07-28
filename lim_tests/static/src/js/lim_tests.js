odoo.define("lim_tests.essayer_une_selle", function (require) {
  "use strict";

  var publicWidget = require("web.public.widget");

  publicWidget.registry.EssayerPage = publicWidget.Widget.extend({
    selector: ".essayer-page-section",
    start: function () {
      this._super.apply(this, arguments);
      console.log("essayer Page Loaded");
    },
  });
});
