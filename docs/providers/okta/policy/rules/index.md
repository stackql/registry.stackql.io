---
title: rules
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
<tr><td><b>Name</b></td><td><code>okta.policy.rules</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.policy.rules</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `conditions` | `object` |  |
| `created` | `string` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
| `system` | `boolean` |  |
| `type` | `string` |  |
| `_embedded` | `object` |  |
| `priority` | `integer` |  |
| `_links` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `policyId, ruleId` | Gets a policy rule. | SELECT |
| `list` | `type` | Gets all policies with the specified type. | SELECT |
| `insert` | `policyId` | Creates a policy rule. | INSERT |
| `delete` | `policyId, ruleId` | Removes a policy rule. | DELETE |
| `activate` | `policyId, ruleId` | Activates a policy rule. | EXEC |
| `deactivate` | `policyId, ruleId` | Deactivates a policy rule. | EXEC |
| `put` | `policyId, ruleId` | Updates a policy rule. | EXEC |
