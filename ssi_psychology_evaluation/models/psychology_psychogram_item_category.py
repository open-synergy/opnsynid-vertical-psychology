# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PsychologyPsychogramItemCategory(models.Model):
    _name = "psychology.psychogram_item_category"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Psychology Psychogram Item Category"

    name = fields.Char(
        string="Item Category",
    )
