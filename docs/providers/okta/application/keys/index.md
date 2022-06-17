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
<tr><td><b>Name</b></td><td><code>okta.application.keys</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.keys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `created` | `string` |  |
| `x5t#S256` | `string` |  |
| `expiresAt` | `string` |  |
| `false` | `string` |  |
| `kty` | `string` |  |
| `lastUpdated` | `string` |  |
| `x5u` | `string` |  |
| `_links` | `object` |  |
| `x5t` | `string` |  |
| `key_ops` | `array` |  |
| `status` | `string` |  |
| `kid` | `string` |  |
| `use` | `string` |  |
| `x5c` | `array` |  |
| `e` | `string` |  |
| `alg` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `appId, keyId` | Gets a specific application key credential by kid | SELECT |
| `list` | `appId` | Enumerates key credentials for an application | SELECT |
| `insert` | `appId` | Generates a new X.509 certificate for an application key credential | INSERT |
| `delete` | `appId, csrId` |  | DELETE |
