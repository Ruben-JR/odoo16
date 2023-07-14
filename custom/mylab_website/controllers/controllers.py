# -*- coding: utf-8 -*-

from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import http, _


class CustomerPortalInherit(CustomerPortal):
    MANDATORY_BILLING_FIELDS = ["name", "date_of_birth", "gender"]
    # OPTIONAL_BILLING_FIELDS = ["mobile", "civil", "country_id", "city", "street2", "county", "zone", "zip"]

    @route(["/my/account"], type="http", auth="user", website=True)
    def account(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        company = request.env.user

        values.update(
            {
                "error": {},
                "error_message": [],
            }
        )
        if post and request.httprequest.method == "POST":
            error, error_message = self.details_form_validate(post)
            values.update({"error": error, "error_message": error_message})
            values.update(post)
            print("Xcn...... ii a", values)
            if not error:
                form_values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                # form_values.update(
                #     {
                #         key: post[key]
                #         for key in self.OPTIONAL_BILLING_FIELDS
                #         if key in post
                #     }
                # )
                for field in set(["country_id", "state_id"]) & set(form_values.keys()):
                    try:
                        form_values[field] = int(form_values[field])
                    except:
                        form_values[field] = False

                form_values.update({"is_patient": True})
                partner.sudo().write(form_values)

                companies = request.env["res.company"].sudo().search([])
                company_ids = [(4, comp.id) for comp in companies]
                company.sudo().write({"company_ids": company_ids})

                if redirect:
                    return request.redirect(redirect)
                return request.redirect("/my/home")

        countries = request.env["res.country"].sudo().search([])
        states = request.env["res.country.state"].sudo().search([])
        values.update(
            {
                "partner": partner,
                "countries": countries,
                "states": states,
                "has_check_vat": hasattr(request.env["res.partner"], "check_vat"),
                "redirect": redirect,
                "page_name": "my_details",
            }
        )

        response = request.render("mylab_website.portal_my_details_inherit", values)
        response.headers.add("X-Frame-Options", "DENY")
        return response
