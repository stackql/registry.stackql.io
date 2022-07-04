---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigateway.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the API. Format: projects/{project}/locations/global/apis/{api} |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `managedService` | `string` | Optional. Immutable. The name of a Google Managed Service ( https://cloud.google.com/service-infrastructure/docs/glossary#managed). If not specified, a new Service will automatically be created in the same project as this API. |
| `state` | `string` | Output only. State of the API. |
| `updateTime` | `string` | Output only. Updated time. |
| `createTime` | `string` | Output only. Created time. |
| `displayName` | `string` | Optional. Display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_get` | `SELECT` | `name` | Gets details of a single Api. |
| `projects_locations_apis_list` | `SELECT` | `parent` | Lists Apis in a given project and location. |
| `projects_locations_apis_create` | `INSERT` | `parent` | Creates a new Api in a given project and location. |
| `projects_locations_apis_delete` | `DELETE` | `name` | Deletes a single Api. |
| `projects_locations_apis_patch` | `EXEC` | `name` | Updates the parameters of a single Api. |
