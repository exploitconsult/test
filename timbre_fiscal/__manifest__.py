# -*- coding: utf-8 -*-
{
    'name': "Droit de timbre",

    'summary': """Le droit de timbre sur les factures
       """,
    'description': """
       Le droit de timbre fixé à 0,600 dinars s'applique aux factures
    """,
    'license': 'AGPL-3',
    'author': "Ahmed Mnasri",
    'website': "http://polyline.xyz",
    'category': 'account',
    'version': '15.0.1',
    'depends': ['product',
                'l10n_tunisia',
                ],
    'data': [
        'data/data.xml',
        'views/product_views.xml',
        'views/invoice_view.xml',

    ],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/Banner.png']
}
