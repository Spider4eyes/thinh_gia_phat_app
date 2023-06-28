from odoo import fields, models, tools


class ProductProduct(models.Model):
    _inherit = "product.product"

    product_handle_id = fields.Many2one(comodel_name="product.handle")
