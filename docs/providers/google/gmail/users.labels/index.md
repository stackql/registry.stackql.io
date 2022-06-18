---
title: users.labels
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
<tr><td><b>Name</b></td><td><code>users.labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gmail.users.labels</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `id, userId` | Gets the specified label. |
| `list` | `SELECT` | `userId` | Lists all labels in the user's mailbox. |
| `create` | `INSERT` | `userId` | Creates a new label. |
| `delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to. |
| `patch` | `EXEC` | `id, userId` | Patch the specified label. |
| `update` | `EXEC` | `id, userId` | Updates the specified label. |
