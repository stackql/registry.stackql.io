---
title: nodeTemplates
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
<tr><td><b>Name</b></td><td><code>nodeTemplates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.nodeTemplates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#nodeTemplate for node templates. |
| `status` | `string` | [Output Only] The status of the node template. One of the following values: CREATING, READY, and DELETING. |
| `disks` | `array` |  |
| `accelerators` | `array` |  |
| `region` | `string` | [Output Only] The name of the region where the node template resides, such as us-central1. |
| `serverBinding` | `object` |  |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `cpuOvercommitType` | `string` | CPU overcommit. |
| `nodeAffinityLabels` | `object` | Labels to use for node affinity, which will be used in instance scheduling. |
| `statusMessage` | `string` | [Output Only] An optional, human-readable explanation of the status. |
| `nodeTypeFlexibility` | `object` |  |
| `nodeType` | `string` | The node type to use for nodes group that are created from this template. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `nodeTemplate, project, region` | Returns the specified node template. Gets a list of available node templates by making a list() request. |
| `list` | `SELECT` | `project, region` | Retrieves a list of node templates available to the specified project. |
| `insert` | `INSERT` | `project, region` | Creates a NodeTemplate resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `nodeTemplate, project, region` | Deletes the specified NodeTemplate resource. |
| `aggregatedList` | `EXEC` | `project` | Retrieves an aggregated list of node templates. |
| `getIamPolicy` | `EXEC` | `project, region, resource` | Gets the access control policy for a resource. May be empty if no such policy or resource exists. |
| `setIamPolicy` | `EXEC` | `project, region, resource` | Sets the access control policy on the specified resource. Replaces any existing policy. |
| `testIamPermissions` | `EXEC` | `project, region, resource` | Returns permissions that a caller has on the specified resource. |
