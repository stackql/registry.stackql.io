---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
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
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Provider. Format: projects/{project}/locations/{location}/providers/{provider} |
| `description` | `string` | Output only. Description of the resource. |
| `documentationUri` | `string` | Output only. Link to documentation page. |
| `launchStage` | `string` | Output only. Flag to mark the version indicating the launch stage. |
| `externalUri` | `string` | Output only. Link to external page. |
| `updateTime` | `string` | Output only. Updated time. |
| `webAssetsLocation` | `string` | Output only. Cloud storage location of icons etc consumed by UI. |
| `labels` | `object` | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `createTime` | `string` | Output only. Created time. |
| `displayName` | `string` | Output only. Display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_providers_get` | `SELECT` | `name` | Gets details of a single Provider. |
| `projects_locations_global_providers_list` | `SELECT` | `parent` | Lists Providers in a given project and location. |
