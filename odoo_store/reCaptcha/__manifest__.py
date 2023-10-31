{
    "name": "MyLab Login/signup reCAPTCHA",
    "version": "12.0.1.0.0",
    "summary": """Protect robot login and signup with reCAPTCHA""",
    "description": """CAPTCHA helps you detect abusive traffic on your website without any user friction.
    The user must register their  domain with CAPTCHA site to get site key add same with our code and use the app.
    login page, signup page,login,signup,protection,site protection,fake login,fake signup,website login,
    website,captcha,captcha,version 12 protectionwebsite protection,robot attack,security,secure login
    ,secure signup""",
    "sequence": -98,
    "author": "Ruben de Pina",
    "company": "Health 360",
    "website": "https://www.health.cv",
    "category": "Extra Tools",
    "depends": [
        "base",
        "auth_signup",
    ],
    "images": ["static/description/banner.gif"],
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "data": ["views/captcha_views.xml"],
    "installable": True,
    "application": True,
    "auto_install": False,
}
