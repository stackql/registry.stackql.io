---
title: projects.locations.clusters.nodePools
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
<tr><td><b>Name</b></td><td><code>projects.locations.clusters.nodePools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.projects.locations.clusters.nodePools</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `clustersId, locationsId, nodePoolsId, projectsId` | Gets the specified operation. |
| `list` | `SELECT` | `clustersId, locationsId, projectsId` | Lists the node pools for a cluster. |
| `create` | `INSERT` | `clustersId, locationsId, projectsId` | Creates a node pool for a cluster. |
| `delete` | `DELETE` | `clustersId, locationsId, nodePoolsId, projectsId` | Deletes a node pool from a cluster. |
| `rollback` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| `setAutoscaling` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the autoscaling settings for the specified node pool. |
| `setManagement` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the NodeManagement options for a node pool. |
| `setSize` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| `update` | `EXEC` | `clustersId, locationsId, nodePoolsId, projectsId` | Updates the version and/or image type for the specified node pool. |
