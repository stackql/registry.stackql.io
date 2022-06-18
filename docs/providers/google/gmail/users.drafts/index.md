---
title: users.drafts
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
<tr><td><b>Name</b></td><td><code>users.drafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gmail.users.drafts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `resultSizeEstimate` | `integer` | Estimated total number of results. |
| `drafts` | `array` | List of drafts. Note that the `Message` property in each `Draft` resource only contains an `id` and a `threadId`. The messages.get method can fetch additional message details. |
| `nextPageToken` | `string` | Token to retrieve the next page of results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `id, userId` | Gets the specified draft. |
| `list` | `SELECT` | `userId` | Lists the drafts in the user's mailbox. |
| `create` | `INSERT` | `userId` | Creates a new draft with the `DRAFT` label. |
| `delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified draft. Does not simply trash it. |
| `send` | `EXEC` | `userId` | Sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers. |
| `update` | `EXEC` | `id, userId` | Replaces a draft's content. |
