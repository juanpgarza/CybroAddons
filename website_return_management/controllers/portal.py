# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Sabeel B (odoo@cybrosys.com)
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
import base64
from collections import OrderedDict
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.tools import image_process
from odoo.tools.translate import _
from odoo.addons.portal.controllers.portal import CustomerPortal


class ReturnCustomerPortal(CustomerPortal):
    """Class to show return orders on portal pages"""
    def _prepare_home_portal_values(self, counters):
        """Fetch total count of sale_return records"""
        values = super()._prepare_home_portal_values(counters)
        if 'return_count' in counters:
            values['return_count'] = request.env['sale.return'].search_count([
                ('state', 'in', ['draft', 'confirm', 'done', 'cancel'])])
        return values

    @http.route(['/my/return_orders',
                 '/my/return_orders/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_my_sale_return(self, page=1, date_begin=None, date_end=None,
                                sortby=None, filterby=None):
        """Return History in my accounts"""
        values = self._prepare_portal_layout_values()
        sale_return = request.env['sale.return']
        domain = []
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
            'sale': {'label': _('Sale Order'), 'order': 'sale_order'},
        }
        # default sort by value
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin),
                       ('create_date', '<=', date_end)]
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': [
                ('state', 'in', ['draft', 'confirm', 'done', 'cancel'])]},
            'confirm': {'label': _('Confirmed'), 'domain': [
                ('state', '=', 'confirm')]},
            'cancel': {'label': _('Cancelled'), 'domain': [
                ('state', '=', 'cancel')]},
            'done': {'label': _('Done'), 'domain': [('state', '=', 'done')]},
        }
        # default filter by value
        if not filterby:
            filterby = 'all'
        domain += searchbar_filters[filterby]['domain']
        # pager
        pager = request.website.pager(
            url="/my/return_orders",
            url_args={'date_begin': date_begin, 'date_end': date_end,
                      'sortby': sortby},
            total=sale_return.search_count(domain),
            page=page,
            step=self._items_per_page
        )
        # content according to pager and archive selected
        orders = sale_return.search(domain, order=order,
                                    limit=self._items_per_page,
                                    offset=pager['offset'])
        request.session['my_return_history'] = orders.ids[:100]
        values.update({
            'date': date_begin,
            'orders': orders.sudo(),
            'page_name': 'Sale_Return',
            'default_url': '/my/return_orders',
            'pager': pager,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("website_return_management.portal_my_returns",
                              values)

    @http.route(['/my/return_orders/<int:order_id>'], type='http',
                auth="public", website=True)
    def portal_my_return_detail(self, order_id=None, access_token=None,
                                report_type=None, download=False, **kw):
        """Passing datas for detailed display in my account"""
        try:
            order_sudo = self._document_check_access('sale.return', order_id,
                                                     access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type,
                                     report_ref='website_return_management.'
                                                'report_sale_returns',
                                     download=download)
        values = self._sale_return_get_page_view_values(order_sudo,
                                                        access_token, **kw)
        return (request.render
                ("website_return_management.portal_sale_return_page", values))

    def _sale_return_get_page_view_values(self, order, access_token, **kwargs):
        def resize_to_48(b64source):
            """Converting product images"""
            if not b64source:
                b64source = request.env['ir.binary']._placeholder()
            else:
                b64source = base64.b64decode(b64source)
            return base64.b64encode(image_process(b64source, size=(48, 48)))
        values = {
            'orders': order,
            'resize_to_48': resize_to_48,
        }
        return self._get_page_view_values(order, access_token, values,
                                          'my_return_history', False, **kwargs)
