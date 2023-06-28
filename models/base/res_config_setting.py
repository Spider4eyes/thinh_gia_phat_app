from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def install_to_set_config(self):
        install_to_set_config = self.env["ir.config_parameter"].sudo().get_param(
            "thinh_gia_phat_app.install_to_set_config"
        )
        if not bool(install_to_set_config):
            config = self.env["res.config.settings"].create({
                "group_product_variant": True,
                "group_uom": True,
            })
            config.execute()
            self.env.ref("base.lang_vi_VN").action_activate_langs()

        return


