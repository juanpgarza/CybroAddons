# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Jumana Jabin MP (odoo@cybrosys.com)
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


class AccountMove(models.Model):
    """Inherited the module for adding a button that helps to send WhatsApp
    message to the customer."""
    _inherit = 'account.move'

    def action_send_by_whatsapp(self):
        """This method is invoked when the 'send_by_whatsapp' button is
         clicked. It opens a wizard containing the message to be sent to the
          WhatsApp web page."""
        if not self.partner_id.mobile:
            raise ValidationError(_('Add a WhatsApp mobile number to the '
                                    ' sale order partner!'))
        if not self.partner_id.mobile.startswith('+'):
            raise ValidationError(_('Please add a valid mobile number along '
                                    ' with a valid country code!'))
        twilio_whatsapp = self.env['ir.config_parameter'].sudo().get_param(
            'all_in_one_whatsapp_integration.twilio_whatsapp')
        if not twilio_whatsapp.startswith('+'):
            raise ValidationError(_('Please add a valid Twilio mobile number '
                                    ' along with "+".'))
        template_id = self.env.ref(
            'all_in_one_whatsapp_integration.account_move_whatsapp_template').id
        mail_template_values = (self.env['mail.template']
                                .browse(template_id).with_context(
            tpl_partners_only=True).generate_email([self.id],
                                                   fields=['body_html']))
        body_html = mail_template_values[self.id].pop('body_html', '')
        whatsapp_message = html2text.html2text(body_html)
        report = self.env.ref("account.account_invoices")._render_qweb_pdf(
            self.ids, data={"report_type": "pdf"})[0]
        report_attachment = self.env['ir.attachment'].sudo().create({
            'name': 'Invoice Report',
            'type': 'binary',
            'datas': base64.b64encode(report),
            "store_fname": base64.b64encode(report),
            'mimetype': 'application/pdf',
            'res_model': 'account.move',
        })
        return {
            'type': 'ir.actions.act_window',
            'name': _('WhatsApp Message'),
            'res_model': 'send.whatsapp.message',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {'default_whatsapp_message': whatsapp_message,
                        'default_attachment_ids': [(4, report_attachment.id)]},
        }
