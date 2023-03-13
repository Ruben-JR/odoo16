import http
import json
from urllib import request
import requests
from openerp.addons.web.controllers.main import Home
from odoo import _


class Extension_Home(Home):
    @http.route(auth="none")
    def web_login(self, redirect=None, **kw):
        if request.httprequest.method == "POST":
            client_key = kw["g-recaptcha-response"]
            secret_key = "6LdU7CEkAAAAAP-zctoLYXRtaKvtiT7Dnpr358F2"
            captcha_data = {"secret": secret_key, "response": client_key}
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", data=captcha_data
            )
            response = json.loads(r.text)
            verify = response["success"]
            if verify:
                # If Google reCaptcha Fill Successfully
                # Your custom logic goes here
                return request.render(
                    "web.login",
                    {
                        "key_1": "Test",
                        "key_2": kw,
                    },
                )
            else:
                values = request.params.copy()
                values["error"] = _("Please Fill Re-Captcha")
                return request.render("web.login", values)
        return super(Extension_Home, self).web_login()
