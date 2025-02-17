# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Ammu (odoo@cybrosys.com)
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
################################################################################

from odoo import api, fields, models


class AccountMoveLine(models.Model):
    """Inherits Invoice Lines"""
    _inherit = 'account.move.line'

    scan_barcode = fields.Char(string='Product Barcode',
                               help="You can scan the barcode here")

    @api.onchange('scan_barcode')
    def _onchange_scan_barcode(self):
        """For getting the scanned barcode product"""
        product_rec = self.env['product.multiple.barcodes']
        if self.scan_barcode:
            self.product_id = product_rec.search(
                [('product_multi_barcode', '=', self.scan_barcode)]).id
