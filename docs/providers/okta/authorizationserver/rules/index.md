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
<tr><td><b>Name</b></td><td><code>okta.authorizationserver.rules</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.rules</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `conditions` | `object` |  |
| `priority` | `integer` |  |
| `created` | `string` |  |
| `system` | `boolean` |  |
| `lastUpdated` | `string` |  |
| `actions` | `object` |  |
| `status` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `authServerId, policyId, ruleId` | Returns a Policy Rule by ID that is defined in the specified Custom Authorization Server and Policy. | SELECT |
| `list` | `authServerId, policyId` | Enumerates all policy rules for the specified Custom Authorization Server and Policy. | SELECT |
| `insert` | `authServerId, policyId` | Creates a policy rule for the specified Custom Authorization Server and Policy. | INSERT |
| `delete` | `authServerId, policyId, ruleId` | Deletes a Policy Rule defined in the specified Custom Authorization Server and Policy. | DELETE |
| `activate` | `authServerId, policyId, ruleId` | Activate Authorization Server Policy Rule | EXEC |
| `deactivate` | `authServerId, policyId, ruleId` | Deactivate Authorization Server Policy Rule | EXEC |
| `update` | `authServerId, policyId, ruleId` | Updates the configuration of the Policy Rule defined in the specified Custom Authorization Server and Policy. | EXEC |
