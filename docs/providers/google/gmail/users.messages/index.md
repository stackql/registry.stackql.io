---
title: users.messages
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
<tr><td><b>Name</b></td><td><code>users.messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gmail.users.messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `messages` | `array` | List of messages. Note that each message resource contains only an `id` and a `threadId`. Additional message details can be fetched using the messages.get method. |
| `nextPageToken` | `string` | Token to retrieve the next page of results in the list. |
| `resultSizeEstimate` | `integer` | Estimated total number of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, userId` | Gets the specified message. |
| `list` | `SELECT` | `userId` | Lists the messages in the user's mailbox. |
| `insert` | `INSERT` | `userId` | Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. Does not send a message. |
| `delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer `messages.trash` instead. |
| `batchDelete` | `EXEC` | `userId` | Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all. |
| `batchModify` | `EXEC` | `userId` | Modifies the labels on the specified messages. |
| `import` | `EXEC` | `userId` | Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message. Note: This function doesn't trigger forwarding rules or filters set up by the user. |
| `modify` | `EXEC` | `id, userId` | Modifies the labels on the specified message. |
| `send` | `EXEC` | `userId` | Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. |
| `trash` | `EXEC` | `id, userId` | Moves the specified message to the trash. |
| `untrash` | `EXEC` | `id, userId` | Removes the specified message from the trash. |
