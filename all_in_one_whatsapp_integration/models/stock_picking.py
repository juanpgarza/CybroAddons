# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Jumana Jabin MP(odoo@cybrosys.com)
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
import base64
import html2text
from odoo import models, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    """Inherited the module for adding a button that helps to send whatsapp
        message to the customer """
    _inherit = 'stock.picking'

    def action_send_by_whatsapp(self):
        """When you click the send_by_whatsapp button, it will open a wizard
         that contain the message to send to the whatsapp web page."""
        if not self.partner_id.mobile:
            raise ValidationError(_('Add whatsapp mobile number to the sale '
                                    ' order partner!'))
        if not self.partner_id.mobile[0] == '+':
            raise ValidationError(_('Please add a valid mobile number along'
                                    '  with a valid country code!'))
        twilio_whatsapp = (self.env['ir.config_parameter']
                           .sudo().get_param('all_in_one_whatsapp_integration.'
                                             'twilio_whatsapp'))
        if twilio_whatsapp[0] != '+':
            raise ValidationError(_('Please add a valid Twilio mobile number '
                                    ' along with "+".'))
        template_id = self.env.ref('all_in_one_whatsapp_integration.'
                                   'stock_picking_whatsapp_template').id
        mail_template_values = (self.env['mail.template']
                                .with_context(tpl_partners_only=True).browse(
            template_id)
                                .generate_email([self.id],
                                                fields=['body_html']))
        body_html = dict(mail_template_values)[self.id].pop('body_html', '')
        whatsapp_message = html2text.html2text(body_html)
        report = self.env.ref('stock.action_report_delivery')._render_qweb_pdf(
            self.ids, data={"report_type": "pdf"})[0]
        report_attachment = self.env['ir.attachment'].sudo().create({
            'name': 'Delivery Report',
            'type': 'binary',
            'datas': base64.b64encode(report),
            'store_fname': base64.b64encode(report),
            'mimetype': 'application/pdf',
            'res_model': 'stock.picking',
        })
        return {
            'type': 'ir.actions.act_window',
            'name': _('Whatsapp Message'),
            'res_model': 'send.whatsapp.message',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {'default_whatsapp_message': whatsapp_message,
                        'default_attachment_ids': [(4,
                                                    report_attachment.id)]},
        }
