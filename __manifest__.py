{
    "name": "Thinh Gia Phat App",
    "author": "Truong Dinh Minh Duc",
    "category": "Cloth Bag Company",
    "version": "16.0.0.0",
    "depends": [
        "base",
        "contacts",
        "product",
        "stock",
        "sale_management",
        "l10n_vn",

        # OCA
        "web_responsive",
        "web_chatter_position",
    ],
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
    "assets": {
        "web.assets_backend": ["thinh_gia_phat_app/static/scss/form_controller.scss"]
    }
}
