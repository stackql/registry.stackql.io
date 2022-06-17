---
title: clientgrants
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
<tr><td><b>Name</b></td><td><code>okta.user.clientgrants</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.clientgrants</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `scopeId` | `string` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
| `created` | `string` |  |
| `issuer` | `string` |  |
| `clientId` | `string` |  |
| `createdBy` | `object` |  |
| `_embedded` | `object` |  |
| `userId` | `string` |  |
| `_links` | `object` |  |
| `source` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `clientId, userId` | Lists all grants for a specified user and client | SELECT |
| `delete` | `clientId, userId` | Revokes all grants for the specified user and client | DELETE |
