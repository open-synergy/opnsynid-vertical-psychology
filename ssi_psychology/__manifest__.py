# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Psychology",
    "version": "14.0.3.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "configuration_helper",
        "mail",
    ],
    "data": [
        "menu.xml",
        "views/res_config_settings_views.xml",
    ],
    "demo": [
        "demo/res_partner_demo.xml",
        "demo/res_users_demo.xml",
    ],
}
