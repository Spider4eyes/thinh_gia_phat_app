from odoo import fields, models, tools


class ProductHandle(models.Model):
    _name = "product.handle"
    _description = "Product Handle"

    name = fields.Char(required=True)
    weight_per_uom = fields.Float(
        help="The weight of handle per 1 unit measure of weight of bag, for ex: 1 kg "
             "bag need 0.2 kg handle"
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
