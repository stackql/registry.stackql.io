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
<tr><td><b>Name</b></td><td><code>okta.user.grants</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.grants</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `issuer` | `string` |  |
| `_links` | `object` |  |
| `_embedded` | `object` |  |
| `created` | `string` |  |
| `lastUpdated` | `string` |  |
| `userId` | `string` |  |
| `createdBy` | `object` |  |
| `source` | `string` |  |
| `status` | `string` |  |
| `scopeId` | `string` |  |
| `clientId` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `grantId, userId` | Gets a grant for the specified user | SELECT |
| `list` | `userId` | Lists all grants for the specified user | SELECT |
| `delete` | `grantId, userId` | Revokes one grant for a specified user | DELETE |
| `deleteAll` | `userId` | Revokes all grants for a specified user | EXEC |
