# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Ammu Raj (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    "name": "Chatter Attachments as ZIP",
    "version": "15.0.1.0.0",
    "category": "Extra Tools",
    "summary": """Download All Chatter Attachments As A Single Zip File.""",
    "description": "This module helps to download all chatter attachments in"
                   "a single zip file",
    "author": "Cybrosys Techno Solutions",
    "company": "Cybrosys Techno Solutions",
    "maintainer": "Cybrosys Techno Solutions",
    "website": "https://www.cybrosys.com",
    "depends": ["mail"],
    "assets": {
        'web.assets_backend': [
            "chatter_attachments_as_zip/static/src/js/attachment_box_inherit_view.js",
        ],
        'web.assets_qweb': [
            ''"chatter_attachments_as_zip/static/src/xml/attachment_box_inherit_view.xml",],
    },
    "images": ["static/description/banner.png"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
