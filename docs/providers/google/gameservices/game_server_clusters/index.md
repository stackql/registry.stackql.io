---
title: game_server_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_clusters
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
<tr><td><b>Name</b></td><td><code>game_server_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gameservices.game_server_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the game server cluster, in the following form: `projects/{project}/locations/{locationId}/realms/{realmId}/gameServerClusters/{gameServerClusterId}`. For example, `projects/my-project/locations/global/realms/zanzibar/gameServerClusters/my-gke-cluster`. |
| `description` | `string` | Human readable description of the cluster. |
| `connectionInfo` | `object` | The game server cluster connection information. |
| `createTime` | `string` | Output only. The creation time. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `labels` | `object` | The labels associated with this game server cluster. Each label is a key-value pair. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `clusterState` | `object` | The state of the Kubernetes cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_realms_gameServerClusters_get` | `SELECT` | `name` | Gets details of a single game server cluster. |
| `projects_locations_realms_gameServerClusters_list` | `SELECT` | `parent` | Lists game server clusters in a given project and location. |
| `projects_locations_realms_gameServerClusters_create` | `INSERT` | `parent` | Creates a new game server cluster in a given project and location. |
| `projects_locations_realms_gameServerClusters_delete` | `DELETE` | `name` | Deletes a single game server cluster. |
| `projects_locations_realms_gameServerClusters_patch` | `EXEC` | `name` | Patches a single game server cluster. |
| `projects_locations_realms_gameServerClusters_previewCreate` | `EXEC` | `parent` | Previews creation of a new game server cluster in a given project and location. |
| `projects_locations_realms_gameServerClusters_previewDelete` | `EXEC` | `name` | Previews deletion of a single game server cluster. |
| `projects_locations_realms_gameServerClusters_previewUpdate` | `EXEC` | `name` | Previews updating a GameServerCluster. |
