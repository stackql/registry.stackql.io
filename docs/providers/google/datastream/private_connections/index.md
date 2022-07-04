---
title: private_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_connections
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
<tr><td><b>Name</b></td><td><code>private_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.private_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource's name. |
| `state` | `string` | Output only. The state of the Private Connection. |
| `updateTime` | `string` | Output only. The update time of the resource. |
| `vpcPeeringConfig` | `object` | The VPC Peering configuration is used to create VPC peering between Datastream and the consumer's VPC. |
| `createTime` | `string` | Output only. The create time of the resource. |
| `displayName` | `string` | Required. Display name. |
| `error` | `object` | Represent a user-facing Error. |
| `labels` | `object` | Labels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_privateConnections_get` | `SELECT` | `name` | Use this method to get details about a private connectivity configuration. |
| `projects_locations_privateConnections_list` | `SELECT` | `parent` | Use this method to list private connectivity configurations in a project and location. |
| `projects_locations_privateConnections_create` | `INSERT` | `parent` | Use this method to create a private connectivity configuration. |
| `projects_locations_privateConnections_delete` | `DELETE` | `name` | Use this method to delete a private connectivity configuration. |
