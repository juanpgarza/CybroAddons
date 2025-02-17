# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Anfas Faisal K (odoo@cybrosys.info)
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


class SaleOrder(models.Model):
    """
    Extends the functionality of the sale.order model in Odoo by adding a
    new field.
    """
    _inherit = 'sale.order'

    customer_image = fields.Binary(string='Image',
                                   related='partner_id.image_1920',
                                   help='The image associated with '
                                        'the partner.')
    theme_id = fields.Many2one('doc.layout', string='Sales',
                               related='company_id.sale_document_layout_id',
                               help='The template to be used for this sale.')


class SaleOrderLine(models.Model):
    """Extends the functionality of the sale.order.line model in Odoo by adding
    a  new field."""
    _inherit = 'sale.order.line'

    order_line_image = fields.Binary(string="Image",
                                     related="product_id.image_128",
                                     help='The image associated with the '
                                          'product of the order line.')
