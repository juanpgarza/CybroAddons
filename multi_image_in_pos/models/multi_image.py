# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: MOHAMMED DILSHAD TK (odoo@cybrosys.com)
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
from odoo import fields, models


class MultiImage(models.Model):
    """ Multiple images for a product """
    _name = 'multi.image'
    _description = 'Multi Image'

    image = fields.Binary(string="Images", help="To upload the Images")
    product_id = fields.Many2one('product.product',
                                 string="Connecting field",
                                 help="Connecting field to the images showing "
                                      "page")
