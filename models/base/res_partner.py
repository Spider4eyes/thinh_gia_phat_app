from odoo import api, fields, models, tools


class ResPartner(models.Model):
    _inherit = "res.partner"

    country_id = fields.Many2one(
        default=lambda self: self.sudo().env.ref("base.vn")
    )
    state_id = fields.Many2one(
        default=lambda self: self.env.ref("base.state_vn_VN-47")
    )
    lang = fields.Selection(default="vi_VN")

    @api.onchange('country_id')
    def _onchange_country_id(self):
        return

    @api.onchange('state_id')
    def _onchange_state(self):
        return
