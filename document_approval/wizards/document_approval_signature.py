# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
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
from odoo import fields, models


class DocumentApprovalSignature(models.TransientModel):
    """ Document approval using signature confirmation"""
    _name = "document.approval.signature"
    _description = "Document signature approvals"
    _rec_name = "document_id"

    note = fields.Text(string='Note', required=True, help='For adding notes')
    signature = fields.Binary(string='Signature', required=True,
                              help='For writing signature')
    document_id = fields.Many2one("document.approval", string="Document",
                                  help="To track which document is get "
                                       "approved ")

    def action_approve_signature(self):
        """ Function to approve document using signature"""
        if self.document_id.team_id.team_lead_id.id == self.env.uid:
            self.document_id.state = "approved"
        else:
            if self.env.uid in self.document_id.approver_ids.ids:
                self.document_id.approval_ids.write({
                    'current_state': 'approved',
                })
                if 'approve' in self.document_id.approval_ids.mapped('state'):
                    self.document_id.state = 'approved'
                    return True
                steps = self.document_id.step_ids.mapped('steps')
                unique_steps = []
                for step in steps:
                    if step not in unique_steps:
                        unique_steps.append(step)
                unique_steps = sorted(unique_steps)
                index_unique = unique_steps.index(self.document_id.step_count)
                if index_unique < len(unique_steps) - 1:
                    next_number = unique_steps[index_unique + 1]
                    self.document_id.step_count = next_number
                    approval_records = self.document_id.step_ids.search(
                        [('steps', '=',
                          next_number), (
                             'document_approve_id',
                             '=',
                             self.document_id.id)])
                    self.document_id.approval_ids = approval_records.ids
                    self.document_id.approval_ids.write({
                        'current_state': 'pending',
                    })
                    users = []
                    for step in approval_records:
                        users.append(step.approver_id.id)
                    self.document_id.approver_ids = users
                else:
                    self.document_id.approval_ids.write({
                        'current_state': 'approved',
                    })
                    self.document_id.state = 'approved'
