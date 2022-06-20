---
title: spaces.messages
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spaces.messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.chat.spaces.messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the attachment, in the form "spaces/*/messages/*/attachments/*". |
| `thumbnailUri` | `string` | Output only. The thumbnail URL which should be used to preview the attachment to a human user. Bots should not use this URL to download attachment content. |
| `attachmentDataRef` | `object` | A reference to the data of an attachment. |
| `contentName` | `string` | The original file name for the content, not the full path. |
| `contentType` | `string` | The content type (MIME type) of the file. |
| `downloadUri` | `string` | Output only. The download URL which should be used to allow a human user to download the attachment. Bots should not use this URL to download attachment content. |
| `driveDataRef` | `object` | A reference to the data of a drive attachment. |
| `source` | `string` | The source of the attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `messagesId, spacesId` | Gets the metadata of a message attachment. The attachment data is fetched using the media API. |
| `create` | `INSERT` | `spacesId` | Creates a message. |
| `delete` | `DELETE` | `messagesId, spacesId` | Deletes a message. |
| `update` | `EXEC` | `messagesId, spacesId` | Updates a message. |
