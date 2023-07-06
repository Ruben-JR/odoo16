/* Copyright 2020 Tecnativa - Alexandre D. Díaz
/* Copyright 2022 Tecnativa - Sergio Teruel
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("mylab_web_pwa.pwa_launch", function (require) {
    "use strict";
    var core = require("web.core");
    var PWAManager = require("mylab_web_pwa.PWAManager");

    core.bus.on("web_client_ready", null, function () {
        this.pwa_manager = new PWAManager(this);
        const def = this.pwa_manager.start();
        return Promise.all([def]);
    });
});
