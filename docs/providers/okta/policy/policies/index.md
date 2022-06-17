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
<tr><td><b>Name</b></td><td><code>okta.policy.policies</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.policy.policies</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `_links` | `object` |  |
| `system` | `boolean` |  |
| `_embedded` | `object` |  |
| `created` | `string` |  |
| `status` | `string` |  |
| `conditions` | `object` |  |
| `priority` | `integer` |  |
| `lastUpdated` | `string` |  |
| `type` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `policyId` | Gets a policy. | SELECT |
| `list` | `type` | Gets all policies with the specified type. | SELECT |
| `insert` | `` | Creates a policy. | INSERT |
| `delete` | `policyId` | Removes a policy. | DELETE |
| `activate` | `policyId, ruleId` | Activates a policy rule. | EXEC |
| `deactivate` | `policyId, ruleId` | Deactivates a policy rule. | EXEC |