---
title: users.settings.sendAs.smimeInfo
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
<tr><td><b>Name</b></td><td><code>users.settings.sendAs.smimeInfo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gmail.users.settings.sendAs.smimeInfo</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `id, sendAsEmail, userId` | Gets the specified S/MIME config for the specified send-as alias. |
| `list` | `SELECT` | `sendAsEmail, userId` | Lists S/MIME configs for the specified send-as alias. |
| `insert` | `INSERT` | `sendAsEmail, userId` | Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key. |
| `delete` | `DELETE` | `id, sendAsEmail, userId` | Deletes the specified S/MIME config for the specified send-as alias. |
| `setDefault` | `EXEC` | `id, sendAsEmail, userId` | Sets the default S/MIME config for the specified send-as alias. |
