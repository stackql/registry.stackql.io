---
title: usertokens
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
<tr><td><b>Name</b></td><td><code>okta.identityprovider.usertokens</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.usertokens</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `token` | `string` |  |
| `tokenAuthScheme` | `string` |  |
| `tokenType` | `string` |  |
| `expiresAt` | `string` |  |
| `scopes` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `idpId, userId` | Fetches the tokens minted by the Social Authentication Provider when the user authenticates with Okta via Social Auth. | SELECT |