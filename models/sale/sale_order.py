from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    pricelist_id = fields.Many2one(default=lambda self: self.env.ref("product.list0"))
    payment_term_id = fields.Many2one(
        default=lambda self: self.env.ref("account.account_payment_term_immediate")
    )
