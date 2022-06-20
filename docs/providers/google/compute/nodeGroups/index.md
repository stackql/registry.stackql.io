---
title: nodeGroups
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
<tr><td><b>Name</b></td><td><code>nodeGroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.nodeGroups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `maintenanceWindow` | `object` | Time window specified for daily maintenance operations. GCE's internal maintenance will be performed within this window. |
| `locationHint` | `string` | An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate. |
| `zone` | `string` | [Output Only] The name of the zone where the node group resides, such as us-central1-a. |
| `size` | `integer` | [Output Only] The total number of nodes in the node group. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#nodeGroup for node group. |
| `autoscalingPolicy` | `object` |  |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `fingerprint` | `string` |  |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `maintenancePolicy` | `string` | Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT, RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies. |
| `status` | `string` |  |
| `nodeTemplate` | `string` | URL of the node template to create the node group from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `nodeGroup, project, zone` | Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead. |
| `list` | `SELECT` | `project, zone` | Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group. |
| `insert` | `INSERT` | `initialNodeCount, project, zone` | Creates a NodeGroup resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `nodeGroup, project, zone` | Deletes the specified NodeGroup resource. |
| `addNodes` | `EXEC` | `nodeGroup, project, zone` | Adds specified number of nodes to the node group. |
| `aggregatedList` | `EXEC` | `project` | Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group. |
| `deleteNodes` | `EXEC` | `nodeGroup, project, zone` | Deletes specified nodes from the node group. |
| `getIamPolicy` | `EXEC` | `project, resource, zone` | Gets the access control policy for a resource. May be empty if no such policy or resource exists. |
| `listNodes` | `EXEC` | `nodeGroup, project, zone` | Lists nodes in the node group. |
| `patch` | `EXEC` | `nodeGroup, project, zone` | Updates the specified node group. |
| `setIamPolicy` | `EXEC` | `project, resource, zone` | Sets the access control policy on the specified resource. Replaces any existing policy. |
| `setNodeTemplate` | `EXEC` | `nodeGroup, project, zone` | Updates the node template of the node group. |
| `testIamPermissions` | `EXEC` | `project, resource, zone` | Returns permissions that a caller has on the specified resource. |
