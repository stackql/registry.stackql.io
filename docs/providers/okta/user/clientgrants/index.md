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
<tr><td><b>Name</b></td><td><code>clientgrants</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.clientgrants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `lastUpdated` | `string` |
| `_links` | `object` |
| `createdBy` | `object` |
| `scopeId` | `string` |
| `status` | `string` |
| `source` | `string` |
| `_embedded` | `object` |
| `clientId` | `string` |
| `userId` | `string` |
| `issuer` | `string` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `clientId, userId` | Lists all grants for a specified user and client |
| `delete` | `DELETE` | `clientId, userId` | Revokes all grants for the specified user and client |
