{
    "name": "Thinh Gia Phat App",
    "author": "Truong Dinh Minh Duc",
    "sequence": 1,
    "category": "Cloth Bag Company",
    "version": "16.0.0.0",
    "depends": ["contacts", "product", "stock", "sale_management", "l10n_vn"],
    "license": "LGPL-3",
    "data": [
        # Data
        "data/installer_data.xml",

        # Security
        "security/ir.model.access.csv",

        # Views
        "views/base/res_partner_view.xml",
        "views/product/product_handle_view.xml",
        "views/product/product_views.xml",
        "views/sale/sale_order_view.xml",

        # Menu
        "menu/sale_menu.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
