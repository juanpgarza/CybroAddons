# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Rahul CK(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO GENERAL
#    PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC
#    LICENSE (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Set Default Filter",
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Make filter as default filter on a click.""",
    'description': """Change filters in search view as default filter and 
     vice versa on enabling the checkbox""",
    'author': "Cybrosys Techno Solutions",
    'company': "Cybrosys Techno Solutions",
    'maintainer': "Cybrosys Techno Solutions",
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'use_by_default_filter/static/src/js/favorite_menu.js',
            'use_by_default_filter/static/src/js/control_panel_model.js'
        ],
        'web.assets_qweb': [
            'use_by_default_filter/static/src/xml/favorite_menu_templates.xml'
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False
}
