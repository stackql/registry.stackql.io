---
title: claims
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
<tr><td><b>Name</b></td><td><code>okta.authorizationserver.claims</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.claims</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `group_filter_type` | `string` |  |
| `value` | `string` |  |
| `system` | `boolean` |  |
| `valueType` | `string` |  |
| `_links` | `object` |  |
| `claimType` | `string` |  |
| `conditions` | `object` |  |
| `status` | `string` |  |
| `alwaysIncludeInToken` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `authServerId, claimId` | Success | SELECT |
| `list` | `authServerId` | Success | SELECT |
| `insert` | `authServerId` | Success | INSERT |
| `delete` | `authServerId, claimId` | Success | DELETE |
| `update` | `authServerId, claimId` | Success | EXEC |