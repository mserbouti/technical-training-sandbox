{
    'name': 'Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Serbouti Mohamed Amine',
    'category': 'Technical',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml'
    ],
    'license': 'LGPL-3',

}