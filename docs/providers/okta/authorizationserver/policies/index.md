---
title: policies
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
<tr><td><b>Name</b></td><td><code>okta.authorizationserver.policies</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.policies</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `_links` | `object` |  |
| `priority` | `integer` |  |
| `lastUpdated` | `string` |  |
| `conditions` | `object` |  |
| `created` | `string` |  |
| `_embedded` | `object` |  |
| `status` | `string` |  |
| `system` | `boolean` |  |
| `type` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `authServerId, policyId` | Success | SELECT |
| `list` | `authServerId` | Success | SELECT |
| `insert` | `authServerId` | Success | INSERT |
| `delete` | `authServerId, policyId` | Success | DELETE |
| `activate` | `authServerId, policyId` | Activate Authorization Server Policy | EXEC |
| `deactivate` | `authServerId, policyId` | Deactivate Authorization Server Policy | EXEC |
| `update` | `authServerId, policyId` | Success | EXEC |
