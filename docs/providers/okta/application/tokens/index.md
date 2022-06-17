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
<tr><td><b>Name</b></td><td><code>okta.application.tokens</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.tokens</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `issuer` | `string` |  |
| `_embedded` | `object` |  |
| `clientId` | `string` |  |
| `userId` | `string` |  |
| `expiresAt` | `string` |  |
| `lastUpdated` | `string` |  |
| `scopes` | `array` |  |
| `_links` | `object` |  |
| `status` | `string` |  |
| `created` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `appId, tokenId` | Gets a token for the specified application | SELECT |
| `list` | `appId` | Lists all tokens for the application | SELECT |
| `delete` | `appId, tokenId` | Revokes the specified token for the specified application | DELETE |
