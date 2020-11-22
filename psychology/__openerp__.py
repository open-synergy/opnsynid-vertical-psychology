# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Vertical Psychology",
    "version": "8.0.1.0.0",
    "author": "PT. Simetri Sinergi Indonesia,OpenSynergy Indonesia",
    "website": "https://simetri-sinergi.id",
    "license": "AGPL-3",
    "depends": [
        "base_sequence_configurator",
        "base_workflow_policy",
        "base_cancel_reason",
        "base_terminate_reason",
        "base_print_policy",
        "base_multiple_approval",
        "web_readonly_bypass",
        "base_ir_filters_active",
        "base_action_rule",
        "account_accountant",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_groups_data.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/base_cancel_reason_configurator_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/product_pricelist_type_data.xml",
        "data/product_pricelist_data.xml",
        "menu.xml",
        "wizards/psychology_create_customer_invoice_from_case_service.xml",
        "wizards/psychology_create_supplier_invoice_from_case_activity.xml",
        "wizards/psychology_finish_activity.xml",
        "wizards/psychology_finish_service.xml",
        "views/psychology_config_setting_views.xml",
        "views/psychology_case_type_views.xml",
        "views/psychology_case_views.xml",
        "views/psychology_case_service_views.xml",
        "views/psychology_case_activity_views.xml",
        "views/res_partner_views.xml",
    ],
    "demo": [
        "demo/product_category_demo.xml",
        "demo/product_demo.xml",
        "demo/res_partner_demo.xml",
        "demo/psychology_case_type_demo.xml",
    ],
    "installable": True,
    "application": True,
}
