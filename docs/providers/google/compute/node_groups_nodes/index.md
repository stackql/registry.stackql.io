---
title: node_groups_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups_nodes
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
<tr><td><b>Name</b></td><td><code>node_groups_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.node_groups_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the node. |
| `status` | `string` |  |
| `disks` | `array` | Local disk configurations. |
| `nodeType` | `string` | The type of this node. |
| `accelerators` | `array` | Accelerators for this node. |
| `cpuOvercommitType` | `string` | CPU overcommit. |
| `serverBinding` | `object` |  |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `serverId` | `string` | Server ID associated with this node. |
| `instances` | `array` | Instances scheduled on this node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `nodeGroups_listNodes` | `SELECT` | `nodeGroup, project, zone` | Lists nodes in the node group. |
| `nodeGroups_addNodes` | `INSERT` | `nodeGroup, project, zone` | Adds specified number of nodes to the node group. |
| `nodeGroups_deleteNodes` | `DELETE` | `nodeGroup, project, zone` | Deletes specified nodes from the node group. |