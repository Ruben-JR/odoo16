# -*- coding: utf-8 -*-
{
    "name": "MyLab Configuration",
    "summary": """All configurations about MyLab modules""",
    "description": """Long description of module's purpose""",
    "author": "Ruben de Pina",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Tools",
    "sequence": -94,
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        # csv file
        # 'security/ir.model.access.csv',
        # data file
        "data/ir_filters_myLab.xml",
        # view file
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
