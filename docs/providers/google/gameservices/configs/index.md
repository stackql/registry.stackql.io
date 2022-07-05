---
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - configs
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gameservices.configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the game server config, in the following form: `projects/{project}/locations/{locationId}/gameServerDeployments/{deploymentId}/configs/{configId}`. For example, `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`. |
| `description` | `string` | The description of the game server config. |
| `fleetConfigs` | `array` | FleetConfig contains a list of Agones fleet specs. Only one FleetConfig is allowed. |
| `labels` | `object` | The labels associated with this game server config. Each label is a key-value pair. |
| `scalingConfigs` | `array` | The autoscaling settings. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `createTime` | `string` | Output only. The creation time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gameServerDeployments_configs_get` | `SELECT` | `name` | Gets details of a single game server config. |
| `projects_locations_gameServerDeployments_configs_list` | `SELECT` | `parent` | Lists game server configs in a given project, location, and game server deployment. |
| `projects_locations_gameServerDeployments_configs_create` | `INSERT` | `parent` | Creates a new game server config in a given project, location, and game server deployment. Game server configs are immutable, and are not applied until referenced in the game server deployment rollout resource. |
| `projects_locations_gameServerDeployments_configs_delete` | `DELETE` | `name` | Deletes a single game server config. The deletion fails if the game server config is referenced in a game server deployment rollout. |
