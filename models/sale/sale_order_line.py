from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_handle_id = fields.Many2one(
        comodel_name="product.handle",
        related="product_id.product_handle_id",
        store=True
    )
    product_handle_weight = fields.Float(
        compute="_compute_product_handle_weight", store=True
    )
    real_qty = fields.Float(compute="_compute_real_qty", store=True)

    @api.depends("product_handle_id", "product_uom_qty")
    def _compute_product_handle_weight(self):
        for rec in self:
            rec.product_handle_weight = rec.product_uom_qty * rec.product_handle_id.weight_per_uom

    @api.depends("product_handle_weight", "product_uom_qty")
    def _compute_real_qty(self):
        for rec in self:
            rec.real_qty = rec.product_uom_qty - rec.product_handle_weight
