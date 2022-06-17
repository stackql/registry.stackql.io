---
title: clienttokens
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
<tr><td><b>Name</b></td><td><code>okta.user.clienttokens</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.user.clienttokens</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `created` | `string` |  |
| `issuer` | `string` |  |
| `clientId` | `string` |  |
| `expiresAt` | `string` |  |
| `_embedded` | `object` |  |
| `lastUpdated` | `string` |  |
| `_links` | `object` |  |
| `userId` | `string` |  |
| `createdBy` | `object` |  |
| `status` | `string` |  |
| `scopes` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `clientId, tokenId, userId` | Gets a refresh token issued for the specified User and Client. | SELECT |
| `list` | `clientId, userId` | Lists all refresh tokens issued for the specified User and Client. | SELECT |
| `delete` | `clientId, tokenId, userId` | Revokes the specified refresh token. | DELETE |
| `deleteAll` | `clientId, userId` | Revokes all refresh tokens issued for the specified User and Client. | EXEC |