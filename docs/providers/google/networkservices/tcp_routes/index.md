---
title: tcp_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - tcp_routes
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
<tr><td><b>Name</b></td><td><code>tcp_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.tcp_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the TcpRoute resource. It matches pattern `projects/*/locations/global/tcpRoutes/tcp_route_name&gt;`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `labels` | `object` | Optional. Set of label tags associated with the TcpRoute resource. |
| `meshes` | `array` | Optional. Meshes defines a list of meshes this TcpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `rules` | `array` | Required. Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `gateways` | `array` | Optional. Gateways defines a list of gateways this TcpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_tcpRoutes_get` | `SELECT` | `name` | Gets details of a single TcpRoute. |
| `projects_locations_tcpRoutes_list` | `SELECT` | `parent` | Lists TcpRoute in a given project and location. |
| `projects_locations_tcpRoutes_create` | `INSERT` | `parent` | Creates a new TcpRoute in a given project and location. |
| `projects_locations_tcpRoutes_delete` | `DELETE` | `name` | Deletes a single TcpRoute. |
| `projects_locations_tcpRoutes_patch` | `EXEC` | `name` | Updates the parameters of a single TcpRoute. |
