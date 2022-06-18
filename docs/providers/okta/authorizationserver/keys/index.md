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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `kid` | `string` |
| `_links` | `object` |
| `alg` | `string` |
| `false` | `string` |
| `e` | `string` |
| `created` | `string` |
| `x5t` | `string` |
| `status` | `string` |
| `x5t#S256` | `string` |
| `kty` | `string` |
| `x5c` | `array` |
| `lastUpdated` | `string` |
| `expiresAt` | `string` |
| `x5u` | `string` |
| `use` | `string` |
| `key_ops` | `array` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `authServerId` |
| `rotate` | `EXEC` | `authServerId` |
