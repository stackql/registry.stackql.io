---
title: game_server_deployments_deployment_state
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_deployments_deployment_state
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
<tr><td><b>Name</b></td><td><code>game_server_deployments_deployment_state</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gameservices.game_server_deployments_deployment_state</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `clusterState` | `array` | The state of the game server deployment in each game server cluster. |
| `unavailable` | `array` | List of locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_gameServerDeployments_fetchDeploymentState` | `SELECT` | `name` |