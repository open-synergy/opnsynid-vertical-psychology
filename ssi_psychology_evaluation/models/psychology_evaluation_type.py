# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PsychologyEvaluationType(models.Model):
    _name = "psychology.evaluation_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Psychology Evaluation Type"

    name = fields.Char(
        string="Type",
    )
    sequence_id = fields.Many2one(
        string="Sequence",
        comodel_name="ir.sequence",
        ondelete="restrict",
    )
    psychogram_ids = fields.Many2many(
        string="Allowed Psychograms",
        comodel_name="psychology.psychogram",
        relation="psychology_rel_evaluation_type_2_psychogram",
        column1="type_id",
        column2="psychogram_id",
    )
    recommedation_ids = fields.Many2many(
        string="Allowed Recommedations",
        comodel_name="psychology.evaluation_recommendation",
        relation="psychology_rel_evaluation_type_2_recommendation",
        column1="type_id",
        column2="recommendation_id",
    )
    psychologist_ids = fields.Many2many(
        string="Allowed Psychologist",
        comodel_name="res.users",
        relation="psychology_rel_evaluation_type_2_psychologist",
        column1="type_id",
        column2="user_id",
    )
