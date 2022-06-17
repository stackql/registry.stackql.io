---
title: idpkeys
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
<tr><td><b>Name</b></td><td><code>okta.identityprovider.idpkeys</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.idpkeys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `e` | `string` |  |
| `x5u` | `string` |  |
| `kid` | `string` |  |
| `_links` | `object` |  |
| `created` | `string` |  |
| `use` | `string` |  |
| `false` | `string` |  |
| `key_ops` | `array` |  |
| `kty` | `string` |  |
| `alg` | `string` |  |
| `expiresAt` | `string` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
| `x5t#S256` | `string` |  |
| `x5t` | `string` |  |
| `x5c` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `idpId, keyId` | Gets a specific IdP Key Credential by `kid` | SELECT |
| `list` | `idpId` | Enumerates signing key credentials for an IdP | SELECT |
| `insert` | `idpId, validityYears` | Generates a new X.509 certificate for an IdP signing key credential to be used for signing assertions sent to the IdP | INSERT |
| `clone` | `idpId, keyId, targetIdpId` | Clones a X.509 certificate for an IdP signing key credential from a source IdP to target IdP | EXEC |
