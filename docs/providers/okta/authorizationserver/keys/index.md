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
| `_links` | `object` |
| `x5t#S256` | `string` |
| `expiresAt` | `string` |
| `e` | `string` |
| `x5c` | `array` |
| `lastUpdated` | `string` |
| `alg` | `string` |
| `use` | `string` |
| `false` | `string` |
| `status` | `string` |
| `kty` | `string` |
| `x5t` | `string` |
| `created` | `string` |
| `key_ops` | `array` |
| `x5u` | `string` |
| `kid` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list` | `SELECT` | `authServerId` |
| `rotate` | `EXEC` | `authServerId` |
