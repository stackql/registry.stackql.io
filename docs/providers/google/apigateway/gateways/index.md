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
<tr><td><b>Id</b></td><td><code>google.apigateway.gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway} |
| `state` | `string` | Output only. The current state of the Gateway. |
| `updateTime` | `string` | Output only. Updated time. |
| `apiConfig` | `string` | Required. Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig} |
| `createTime` | `string` | Output only. Created time. |
| `defaultHostname` | `string` | Output only. The default API Gateway host name of the form `{gateway_id}-{hash}.{region_code}.gateway.dev`. |
| `displayName` | `string` | Optional. Display name. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gateways_get` | `SELECT` | `name` | Gets details of a single Gateway. |
| `projects_locations_gateways_list` | `SELECT` | `parent` | Lists Gateways in a given project and location. |
| `projects_locations_gateways_create` | `INSERT` | `parent` | Creates a new Gateway in a given project and location. |
| `projects_locations_gateways_delete` | `DELETE` | `name` | Deletes a single Gateway. |
| `projects_locations_gateways_patch` | `EXEC` | `name` | Updates the parameters of a single Gateway. |