---
title: keys
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
<tr><td><b>Name</b></td><td><code>okta.authorizationserver.keys</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.keys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `x5t#S256` | `string` |  |
| `status` | `string` |  |
| `kty` | `string` |  |
| `kid` | `string` |  |
| `_links` | `object` |  |
| `e` | `string` |  |
| `x5c` | `array` |  |
| `x5u` | `string` |  |
| `use` | `string` |  |
| `expiresAt` | `string` |  |
| `alg` | `string` |  |
| `x5t` | `string` |  |
| `false` | `string` |  |
| `key_ops` | `array` |  |
| `created` | `string` |  |
| `lastUpdated` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list` | `authServerId` | Success | SELECT |
| `rotate` | `authServerId` | Success | EXEC |
