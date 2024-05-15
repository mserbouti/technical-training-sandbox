{
    "name": "Estate",
    "version": "1.0",
    "depends": ["base"],
    "author": "Serbouti Mohamed Amine",
    "category": "Real Estate/Brokerage",
    "description": """
    Description text
    """,
    # data files always loaded at installation
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_type_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
        "views/hello.xml",
    ],
    "demo": [
        "demo/estate.property.type.csv",
        "demo/estate_property.xml",
        "demo/estate_property_offers.xml",
    ],
    "assets": {
        "estate.assets_hello": [
            ("include", "web._assets_helpers"),
            "web/static/src/scss/pre_variables.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            ("include", "web._assets_bootstrap"),
            ("include", "web._assets_core"),
            "estate/static/src/hello/**/*",
        ],
    },
    "application": True,
    "license": "LGPL-3",
}
