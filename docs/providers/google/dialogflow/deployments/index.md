---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the deployment. Format: projects//locations//agents//environments//deployments/. |
| `flowVersion` | `string` | The name of the flow version for this deployment. Format: projects//locations//agents//flows//versions/. |
| `result` | `object` | Result of the deployment. |
| `startTime` | `string` | Start time of this deployment. |
| `state` | `string` | The current state of the deployment. |
| `endTime` | `string` | End time of this deployment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_environments_deployments_get` | `SELECT` | `name` | Retrieves the specified Deployment. |
| `projects_locations_agents_environments_deployments_list` | `SELECT` | `parent` | Returns the list of all deployments in the specified Environment. |
