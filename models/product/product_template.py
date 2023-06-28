from odoo import fields, models, tools


class ProductTemplate(models.Model):
    _inherit = "product.template"

    uom_id = fields.Many2one(default=lambda self: self.env.ref("uom.product_uom_kgm"))
    detailed_type = fields.Selection(default="product")
