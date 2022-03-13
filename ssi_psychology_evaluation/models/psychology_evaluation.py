# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class PsychologyEvaluation(models.Model):
    _name = "psychology.evaluation"
    _inherit = [
        "mixin.transaction_confirm",
        "mixin.transaction_done",
        "mixin.transaction_cancel",
    ]
    _description = "Psychology Evaluation"
    _approval_from_state = "draft"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    type_id = fields.Many2one(
        string="Type",
        copy=True,
        required=True,
        ondelete="restrict",
        comodel_name="psychology.evaluation_type",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    psychogram_ids = fields.Many2many(
        string="Allowed Psychograms",
        comodel_name="psychology.psychogram",
        related="type_id.psychogram_ids",
    )
    psychogram_id = fields.Many2one(
        string="Psychogram",
        copy=True,
        required=True,
        ondelete="restrict",
        comodel_name="psychology.psychogram",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    psychologist_ids = fields.Many2many(
        string="Allowed Psychologist",
        comodel_name="res.users",
        related="type_id.psychologist_ids",
    )
    psychologist_id = fields.Many2one(
        string="Psychologist",
        copy=True,
        required=True,
        ondelete="restrict",
        comodel_name="res.users",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    user_id = fields.Many2one(
        string="Responsible",
        copy=True,
        required=True,
        ondelete="restrict",
        comodel_name="res.users",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    client_id = fields.Many2one(
        string="Client",
        copy=True,
        required=True,
        ondelete="restrict",
        comodel_name="res.partner",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    date_report = fields.Date(
        string="Evaluation Date",
        index=True,
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=True,
        default=fields.Date.context_today,
    )
    description = fields.Text(
        string="Description",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    conclusion = fields.Text(
        string="Conclusion",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    advise = fields.Text(
        string="Advise",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    detail_ids = fields.One2many(
        string="Details",
        comodel_name="psychology.evaluation_detail",
        inverse_name="evaluation_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
            ("reject", "Rejected"),
        ],
        default="draft",
        copy=False,
    )

    @api.depends("policy_template_id")
    def _compute_policy(self):
        _super = super(PsychologyEvaluation, self)
        _super._compute_policy()

    @api.onchange(
        "type_id",
    )
    def onchange_psychogram_id(self):
        self.psychogram_id = False

    @api.onchange(
        "type_id",
    )
    def onchange_psychologist_id(self):
        self.psychologist_id = False

    @api.onchange(
        "type_id",
    )
    def onchange_policy_template_id(self):
        template_id = self._get_template_policy()
        self.policy_template_id = template_id

    def action_reload_detail(self):
        for record in self:
            record._reload_detail()

    def _reload_detail(self):
        self.ensure_one()
        if self.psychogram_id:
            self.detail_ids.unlink()
            self.write(self._prepare_evaluation_detail())

    def _prepare_evaluation_detail(self):
        self.ensure_one()
        result = []
        for detail in self.psychogram_id.detail_ids:
            result.append(detail._prepare_evaluation_detail())
        return {
            "detail_ids": result,
        }
