from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_handle_id = fields.Many2one(
        comodel_name="product.handle",
        related="product_id.product_handle_id",
        store=True
    )
    product_uom_qty = fields.Float(
        string="Khối lượng yêu cầu", default=10, digits=(15, 1)
    )
    handle_quantity = fields.Integer(related="product_handle_id.quantity", store=True)
    handle_weight = fields.Float(related="product_handle_id.weight", store=True)
    estimated_ordered_product_quantity = fields.Float(
        string="Số Túi Nhận",
        compute="_compute_estimated_ordered_product_quantity",
        help="Chỉ có khi túi có quai, nếu số túi = 1, có nghĩa là túi ko có quai. Lúc "
             "đó, khối lượng sẽ là khối lượng túi của tất cả túi",
        store=True
    )
    estimated_ordered_handle_weight = fields.Float(
        string="Trọng Lượng Quai",
        compute="_compute_estimated_ordered_handle_weight",
        store=True
    )
    ordered_product_weight = fields.Float(
        string="Trọng Lượng Túi",
        compute="_compute_ordered_product_weight",
        store=True
    )

    @api.depends("product_handle_id", "handle_quantity", "product_uom_qty")
    def _compute_estimated_ordered_product_quantity(self):
        for rec in self:
            if rec.product_handle_id:
                rec.estimated_ordered_product_quantity = round(
                    rec.product_uom_qty * rec.handle_quantity / 10, 1
                )
            else:
                rec.estimated_ordered_product_quantity = 1

    @api.depends("handle_weight", "product_handle_id", "product_uom_qty")
    def _compute_estimated_ordered_handle_weight(self):
        for rec in self:
            if rec.product_handle_id:
                rec.estimated_ordered_handle_weight = round(
                    rec.product_uom_qty * rec.handle_weight / 10, 1
                )
            else:
                rec.estimated_ordered_handle_weight = 0

    @api.depends("product_handle_id", "product_uom_qty", "estimated_ordered_handle_weight")
    def _compute_ordered_product_weight(self):
        for rec in self:
            rec.ordered_product_weight = rec.product_uom_qty - rec.estimated_ordered_handle_weight

    @api.onchange('product_id')
    def _onchange_product_id_warning(self):
        super(SaleOrderLine, self)._onchange_product_id_warning()
        # Force the user default product_uom_qty = 10, if the user change the product
        if self.product_uom_qty == 1:
            self.product_uom_qty = 10
