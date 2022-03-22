# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Psychology Evaluation",
    "version": "14.0.2.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "ssi_psychology",
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_open_mixin",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/approval_template_data.xml",
        "data/policy_template_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "views/psychology_psychogram_item_value_views.xml",
        "views/psychology_psychogram_item_value_set_views.xml",
        "views/psychology_psychogram_item_category_views.xml",
        "views/psychology_evaluation_recommendation_views.xml",
        "views/psychology_evaluation_result_views.xml",
        "views/psychology_evaluation_purpose_views.xml",
        "views/psychology_psychogram_views.xml",
        "views/psychology_evaluation_type_views.xml",
        "views/psychology_evaluation_views.xml",
        "views/psychology_evaluation_batch_views.xml",
    ],
    "demo": [
        "demo/psychology_evaluation_purpose_demo.xml",
        "demo/psychology_evaluation_result_demo.xml",
        "demo/psychology_psychogram_item_value_demo.xml",
        "demo/psychology_psychogram_item_value_set_demo.xml",
        "demo/psychology_psychogram_demo.xml",
        "demo/psychology_evaluation_type_demo.xml",
    ],
}
