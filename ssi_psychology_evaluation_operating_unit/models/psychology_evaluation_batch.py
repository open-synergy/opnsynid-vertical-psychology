# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class PsychologyEvaluationBatch(models.Model):
    _name = "psychology.evaluation_batch"
    _inherit = [
        "psychology.evaluation_batch",
        "mixin.single_operating_unit",
    ]
