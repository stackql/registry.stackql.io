---
title: projects.zones.clusters.nodePools
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
<tr><td><b>Name</b></td><td><code>projects.zones.clusters.nodePools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.projects.zones.clusters.nodePools</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `clusterId, nodePoolId, projectId, zone` | Retrieves the requested node pool. |
| `list` | `SELECT` | `clusterId, projectId, zone` | Lists the node pools for a cluster. |
| `create` | `INSERT` | `clusterId, projectId, zone` | Creates a node pool for a cluster. |
| `delete` | `DELETE` | `clusterId, nodePoolId, projectId, zone` | Deletes a node pool from a cluster. |
| `autoscaling` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the autoscaling settings for the specified node pool. |
| `rollback` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| `setManagement` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the NodeManagement options for a node pool. |
| `setSize` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| `update` | `EXEC` | `clusterId, nodePoolId, projectId, zone` | Updates the version and/or image type for the specified node pool. |
