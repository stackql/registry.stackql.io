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
<tr><td><b>Name</b></td><td><code>okta.identityprovider.keys</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.keys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `x5t#S256` | `string` |  |
| `x5c` | `array` |  |
| `false` | `string` |  |
| `use` | `string` |  |
| `expiresAt` | `string` |  |
| `kid` | `string` |  |
| `status` | `string` |  |
| `e` | `string` |  |
| `kty` | `string` |  |
| `x5u` | `string` |  |
| `lastUpdated` | `string` |  |
| `key_ops` | `array` |  |
| `created` | `string` |  |
| `_links` | `object` |  |
| `alg` | `string` |  |
| `x5t` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `keyId` | Gets a specific IdP Key Credential by `kid` | SELECT |
| `list` | `` | Enumerates IdP key credentials. | SELECT |
| `insert` | `` | Adds a new X.509 certificate credential to the IdP key store. | INSERT |
| `delete` | `keyId` | Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP. | DELETE |
