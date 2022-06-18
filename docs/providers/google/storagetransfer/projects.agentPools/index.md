---
title: projects.agentPools
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
<tr><td><b>Name</b></td><td><code>projects.agentPools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storagetransfer.projects.agentPools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `agentPools` | `array` | A list of agent pools. |
| `nextPageToken` | `string` | The list next page token. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `agentPoolsId, filter, projectsId` | Lists transfer operations. Operations are ordered by their creation time in reverse chronological order. |
| `list` | `SELECT` | `projectsId` | Lists agent pools. |
| `create` | `INSERT` | `projectsId` | Creates an agent pool resource. |
| `delete` | `DELETE` | `agentPoolsId, projectsId` | Deletes an agent pool. |
| `patch` | `EXEC` | `agentPoolsId, projectsId` | Updates an existing agent pool resource. |
