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
<tr><td><b>Name</b></td><td><code>okta.authorizationserver.tokens</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.tokens</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `status` | `string` |  |
| `_embedded` | `object` |  |
| `lastUpdated` | `string` |  |
| `issuer` | `string` |  |
| `_links` | `object` |  |
| `clientId` | `string` |  |
| `createdBy` | `object` |  |
| `scopes` | `array` |  |
| `created` | `string` |  |
| `expiresAt` | `string` |  |
| `userId` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `authServerId, clientId, tokenId` | Success | SELECT |
| `list` | `authServerId, clientId` | Success | SELECT |
| `delete` | `authServerId, clientId, tokenId` | Success | DELETE |
| `deleteall` | `authServerId, clientId` | Success | EXEC |
