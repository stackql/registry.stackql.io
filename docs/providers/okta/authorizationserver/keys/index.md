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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `false` | `string` |
| `lastUpdated` | `string` |
| `created` | `string` |
| `_links` | `object` |
| `e` | `string` |
| `expiresAt` | `string` |
| `kid` | `string` |
| `kty` | `string` |
| `key_ops` | `array` |
| `x5u` | `string` |
| `status` | `string` |
| `use` | `string` |
| `alg` | `string` |
| `x5c` | `array` |
| `x5t#S256` | `string` |
| `x5t` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `authServerId` |
| `rotate` | `EXEC` | `authServerId` |
