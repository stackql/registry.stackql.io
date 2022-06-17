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
<tr><td><b>Id</b></td><td><code>okta.application.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `_links` | `object` |
| `e` | `string` |
| `kty` | `string` |
| `alg` | `string` |
| `x5t#S256` | `string` |
| `x5u` | `string` |
| `false` | `string` |
| `x5c` | `array` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `created` | `string` |
| `kid` | `string` |
| `x5t` | `string` |
| `use` | `string` |
| `key_ops` | `array` |
| `expiresAt` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `appId, keyId` | Gets a specific application key credential by kid |
| `list` | `SELECT` | `appId` | Enumerates key credentials for an application |
| `insert` | `INSERT` | `appId` | Generates a new X.509 certificate for an application key credential |
| `delete` | `DELETE` | `appId, csrId` |  |
