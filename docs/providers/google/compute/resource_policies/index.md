---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
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
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.resource_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` |  |
| `selfLink` | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| `snapshotSchedulePolicy` | `object` | A snapshot schedule policy specifies when and how frequently snapshots are to be created for the target disk. Also specifies how many and how long these scheduled snapshots should be retained. |
| `resourceStatus` | `object` | Contains output only fields. Use this sub-message for all output fields set on ResourcePolicy. The internal structure of this "status" field should mimic the structure of ResourcePolicy proto specification. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `instanceSchedulePolicy` | `object` | An InstanceSchedulePolicy specifies when and how frequent certain operations are performed on the instance. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#resource_policies for resource policies. |
| `region` | `string` |  |
| `groupPlacementPolicy` | `object` | A GroupPlacementPolicy specifies resource placement configuration. It specifies the failure bucket separation as well as network locality |
| `status` | `string` | [Output Only] The status of resource policy creation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `resourcePolicies_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of resource policies. |
| `resourcePolicies_get` | `SELECT` | `project, region, resourcePolicy` | Retrieves all information of the specified resource policy. |
| `resourcePolicies_list` | `SELECT` | `project, region` | A list all the resource policies that have been configured for the specified project in specified region. |
| `resourcePolicies_insert` | `INSERT` | `project, region` | Creates a new resource policy. |
| `resourcePolicies_delete` | `DELETE` | `project, region, resourcePolicy` | Deletes the specified resource policy. |
