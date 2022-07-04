---
title: grpc_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - grpc_routes
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
<tr><td><b>Name</b></td><td><code>grpc_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.grpc_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the GrpcRoute resource. It matches pattern `projects/*/locations/global/grpcRoutes/` |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `meshes` | `array` | Optional. Meshes defines a list of meshes this GrpcRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` |
| `hostnames` | `array` | Required. Service hostnames with an optional port for which this route describes traffic. Format: [:] Hostname is the fully qualified domain name of a network host. This matches the RFC 1123 definition of a hostname with 2 notable exceptions: - IPs are not allowed. - A hostname may be prefixed with a wildcard label (*.). The wildcard label must appear by itself as the first label. Hostname can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.example.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. *.example.com). Note that as per RFC1035 and RFC1123, a label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character. No other punctuation is allowed. The routes associated with a Mesh or Gateway must have unique hostnames. If you attempt to attach multiple routes with conflicting hostnames, the configuration will be rejected. For example, while it is acceptable for routes for the hostnames "*.foo.bar.com" and "*.bar.com" to be associated with the same route, it is not possible to associate two routes both with "*.bar.com" or both with "bar.com". If a port is specified, then gRPC clients must use the channel URI with the port to match this rule (i.e. "xds:///service:123"), otherwise they must supply the URI without a port (i.e. "xds:///service"). |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
| `labels` | `object` | Optional. Set of label tags associated with the GrpcRoute resource. |
| `gateways` | `array` | Optional. Gateways defines a list of gateways this GrpcRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/` |
| `rules` | `array` | Required. A list of detailed rules defining how to route traffic. Within a single GrpcRoute, the GrpcRoute.RouteAction associated with the first matching GrpcRoute.RouteRule will be executed. At least one rule must be supplied. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_grpcRoutes_get` | `SELECT` | `name` | Gets details of a single GrpcRoute. |
| `projects_locations_grpcRoutes_list` | `SELECT` | `parent` | Lists GrpcRoutes in a given project and location. |
| `projects_locations_grpcRoutes_create` | `INSERT` | `parent` | Creates a new GrpcRoute in a given project and location. |
| `projects_locations_grpcRoutes_delete` | `DELETE` | `name` | Deletes a single GrpcRoute. |
| `projects_locations_grpcRoutes_patch` | `EXEC` | `name` | Updates the parameters of a single GrpcRoute. |