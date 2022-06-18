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
<tr><td><b>Id</b></td><td><code>okta.identityprovider.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `alg` | `string` |
| `lastUpdated` | `string` |
| `e` | `string` |
| `false` | `string` |
| `x5t` | `string` |
| `created` | `string` |
| `x5t#S256` | `string` |
| `x5c` | `array` |
| `expiresAt` | `string` |
| `_links` | `object` |
| `x5u` | `string` |
| `key_ops` | `array` |
| `use` | `string` |
| `kid` | `string` |
| `kty` | `string` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `keyId` | Gets a specific IdP Key Credential by `kid` |
| `list` | `SELECT` |  | Enumerates IdP key credentials. |
| `insert` | `INSERT` |  | Adds a new X.509 certificate credential to the IdP key store. |
| `delete` | `DELETE` | `keyId` | Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP. |