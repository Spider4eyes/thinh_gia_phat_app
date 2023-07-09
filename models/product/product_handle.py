from odoo import fields, models, tools


class ProductHandle(models.Model):
    _name = "product.handle"
    _description = "Product Handle"

    name = fields.Char(required=True)
    quantity = fields.Integer(
        required=True,
        string="Số lượng",
        help="Số lượng túi(túi + quai) ước tính trên 10kg"
    )
    weight = fields.Float(
        string="Khối lượng quai",
        required=True,
        help="Khối lượng kg của quai trên 10 kg tổng (túi + quai)"
    )
    active = fields.Boolean(default=True)
    uom_id = fields.Many2one(
        "uom.uom", "Unit of Measure",
        default=lambda self: self.env.ref("uom.product_uom_kgm"),
        readonly=True,
    )
    weight_uom_name = fields.Char(
        string="Weight Name",
        related="uom_id.name",
        store=True,
    )
