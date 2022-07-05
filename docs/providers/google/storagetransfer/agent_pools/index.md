---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
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
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storagetransfer.agent_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Specifies a unique string that identifies the agent pool. Format: `projects/{project_id}/agentPools/{agent_pool_id}` |
| `state` | `string` | Output only. Specifies the state of the AgentPool. |
| `bandwidthLimit` | `object` | Specifies a bandwidth limit for an agent pool. |
| `displayName` | `string` | Specifies the client-specified AgentPool description. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_agentPools_get` | `SELECT` | `name` | Gets an agent pool. |
| `projects_agentPools_list` | `SELECT` | `projectId` | Lists agent pools. |
| `projects_agentPools_create` | `INSERT` | `projectId` | Creates an agent pool resource. |
| `projects_agentPools_delete` | `DELETE` | `name` | Deletes an agent pool. |
| `projects_agentPools_patch` | `EXEC` | `name` | Updates an existing agent pool resource. |
