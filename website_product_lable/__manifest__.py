# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2021 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Product Ribbon',
    'category': 'Website',
    'summary': 'Website Product Ribbon',

    'version': '0.1',
    'description': """
Website Product Label
==================
        This module allows show product label as Ribbon in Shop Page which is attract product to customer for shopping.
        """,

    'author': 'Odoo Helper',
    'license': 'AGPL-3',

    'depends': [
        'base','website','website_sale'
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/product_label_view.xml',
        'views/template.xml',
    ],
    'images': ['images/OdooHelper.jpeg'],
    'price': 14.24,
    'currency': 'USD',

    'installable': True,
    'application': False
}
