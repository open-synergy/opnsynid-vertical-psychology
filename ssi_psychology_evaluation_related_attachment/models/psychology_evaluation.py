# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class PsychologyEvaluation(models.Model):
    _name = "psychology.evaluation"
    _inherit = [
        "psychology.evaluation",
        "mixin.related_attachment",
    ]
