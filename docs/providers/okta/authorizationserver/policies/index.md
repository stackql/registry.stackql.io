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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `status` | `string` |
| `_links` | `object` |
| `system` | `boolean` |
| `_embedded` | `object` |
| `created` | `string` |
| `conditions` | `object` |
| `type` | `string` |
| `lastUpdated` | `string` |
| `priority` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `authServerId, policyId` | Success |
| `list` | `SELECT` | `authServerId` | Success |
| `insert` | `INSERT` | `authServerId` | Success |
| `delete` | `DELETE` | `authServerId, policyId` | Success |
| `activate` | `EXEC` | `authServerId, policyId` | Activate Authorization Server Policy |
| `deactivate` | `EXEC` | `authServerId, policyId` | Deactivate Authorization Server Policy |
| `update` | `EXEC` | `authServerId, policyId` | Success |
