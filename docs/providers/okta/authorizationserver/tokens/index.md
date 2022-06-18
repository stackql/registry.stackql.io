---
title: tokens
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `createdBy` | `object` |
| `issuer` | `string` |
| `scopes` | `array` |
| `status` | `string` |
| `_links` | `object` |
| `lastUpdated` | `string` |
| `created` | `string` |
| `_embedded` | `object` |
| `clientId` | `string` |
| `expiresAt` | `string` |
| `userId` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `authServerId, clientId, tokenId` |
| `list` | `SELECT` | `authServerId, clientId` |
| `delete` | `DELETE` | `authServerId, clientId, tokenId` |
| `deleteall` | `EXEC` | `authServerId, clientId` |