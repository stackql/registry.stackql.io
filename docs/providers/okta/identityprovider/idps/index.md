---
title: idps
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
<tr><td><b>Name</b></td><td><code>okta.identityprovider.idps</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.idps</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `_links` | `object` |  |
| `status` | `string` |  |
| `created` | `string` |  |
| `lastUpdated` | `string` |  |
| `issuerMode` | `string` |  |
| `policy` | `object` |  |
| `protocol` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `idpId` | Fetches an IdP by `id`. | SELECT |
| `list` | `` | Enumerates IdPs in your organization with pagination. A subset of IdPs can be returned that match a supported filter expression or query. | SELECT |
| `insert` | `` | Adds a new IdP to your organization. | INSERT |
| `delete` | `idpId` | Removes an IdP from your organization. | DELETE |
| `activate` | `idpId` | Activates an inactive IdP. | EXEC |
| `deactivate` | `idpId` | Activates an inactive IdP. | EXEC |
| `update` | `idpId` | Updates the configuration for an IdP. | EXEC |
