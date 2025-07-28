{
    "name": "Custom Theme",
    "description": "Custom Theme",
    "version": "1.0",
    "author": "serbouti med amine",
    "category": "Theme/Creative",
    "depends": ["website"],
    "data": [
        "views/website_templates.xml",
        "data/presets.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            ("prepend", "website_airproof/static/src/scss/primary_variables.scss"),
        ],
        "web.assets_frontend": [
            "website_airproof/static/src/scss/font.scss",
            "website_airproof/static/src/js/script.js",
            "/web/static/src/libs/fontawesome/fonts/fontawesome-webfont.woff2?v=4.7.0",
        ],
    },
    "images": ["static/src/img/wbuilde/aa.png"],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
