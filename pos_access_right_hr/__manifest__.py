# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Fathima Mazlin AM (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'POS Access Right',
    'version': '15.0.1.0.0',
    "category": 'Point of Sale',
    'summary': 'To Restrict POS features for cashiers',
    'description': 'This app allows you to enable or disable POS features '
                   'depending on the access rights granted to the cashiers',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com/',
    'depends': ['base', 'pos_hr'],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_access_right_hr/static/src/js/models.js',
            'pos_access_right_hr/static/src/js/NumpadWidget.js',
            'pos_access_right_hr/static/src/js/ActionpadWidget.js',
        ],
        'web.assets_qweb': [
            'pos_access_right_hr/static/src/xml/NumpadWidget.xml',
            'pos_access_right_hr/static/src/xml/ActionpadWidget.xml'
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
