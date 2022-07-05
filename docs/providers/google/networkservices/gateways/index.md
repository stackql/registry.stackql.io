---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `scope` | `string` | Required. Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens. |
| `serverTlsPolicy` | `string` | Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `selfLink` | `string` | Output only. Server-defined URL of this resource |
| `labels` | `object` | Optional. Set of label tags associated with the Gateway resource. |
| `type` | `string` | Immutable. The type of the customer managed gateway. |
| `ports` | `array` | Required. One or more ports that the Gateway must receive traffic on. The proxy binds to the ports specified. Gateway listen on 0.0.0.0 on the ports specified below. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gateways_get` | `SELECT` | `name` | Gets details of a single Gateway. |
| `projects_locations_gateways_list` | `SELECT` | `parent` | Lists Gateways in a given project and location. |
| `projects_locations_gateways_create` | `INSERT` | `parent` | Creates a new Gateway in a given project and location. |
| `projects_locations_gateways_delete` | `DELETE` | `name` | Deletes a single Gateway. |
| `projects_locations_gateways_patch` | `EXEC` | `name` | Updates the parameters of a single Gateway. |
