/** @odoo-module **/

import { AttachmentBox } from '@mail/components/attachment_box/attachment_box';
import { patch } from 'web.utils';
const Dialog = require('web.Dialog');


patch(AttachmentBox.prototype, 'chatter_attachments_as_zip/static/src/js/attachment_box_inherit_view.js', {
    onClickDownloadAttachment(ev) {
            // Check if there are attachments available
            if (this.chatter.thread && this.chatter.thread.allAttachments.length == 0) {
                Dialog.alert(
                this,
                "There are no attachments to download.",
                    );
                return;
            }
            // Build the URL with parameters in the query string
            const url = `/chatter/attachments/download/zip?res_id=${this.chatter.threadId}`;
            // Send an HTTP GET request to download attachments as a zip file
            fetch(url)
                .then(response => {
                    if (response.ok) {
                        // Create a Blob from the response data
                        return response.blob();
                    } else {
                        throw new Error('Failed to fetch');
                    }
                })
                .then(blob => {
                    // Create a URL for the Blob
                    const blobUrl = URL.createObjectURL(blob);
                    // Create an anchor element for downloading
                    const link = document.createElement('a');
                    link.href = blobUrl;
                    link.download = `attachments${this.chatter.threadId}.zip`;
                    // Trigger a click event to start the download
                    link.click();
                    // Clean up by revoking the Blob URL
                    URL.revokeObjectURL(blobUrl);
                })
        }
})
