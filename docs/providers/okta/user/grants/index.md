---
title: grants
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
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.grants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `userId` | `string` |
| `created` | `string` |
| `createdBy` | `object` |
| `clientId` | `string` |
| `issuer` | `string` |
| `lastUpdated` | `string` |
| `scopeId` | `string` |
| `_links` | `object` |
| `source` | `string` |
| `status` | `string` |
| `_embedded` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `grantId, userId` | Gets a grant for the specified user |
| `list` | `SELECT` | `userId` | Lists all grants for the specified user |
| `delete` | `DELETE` | `grantId, userId` | Revokes one grant for a specified user |
| `deleteAll` | `EXEC` | `userId` | Revokes all grants for a specified user |
