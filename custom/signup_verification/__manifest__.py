# -*- coding: utf-8 -*-
{
    "name": "health_signup_verification",
    "summary": """User signUp email and number vefication""",
    "description": """After user create an account he need to confirm email and phone number to proceed to login""",
    "author": "Ruben de Pina",
    "website": "https://www.health.cv",
    "category": "Health",
    "version": "0.1",
    "depends": [
        "base",
        "auth_signup",
    ],
    "data": ["views/views.xml", "data/email.xml", "data/config.xml"],
    "installable": True,
    "license": "LGPL-3",
    "application": True,
    "auto_install": False,
}
