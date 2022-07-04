---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The Source name. |
| `description` | `string` | User-provided description of the source. |
| `vmware` | `object` | VmwareSourceDetails message describes a specific source details for the vmware source type. |
| `createTime` | `string` | Output only. The create time timestamp. |
| `labels` | `object` | The labels of the source. |
| `updateTime` | `string` | Output only. The update time timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sources_get` | `SELECT` | `name` | Gets details of a single Source. |
| `projects_locations_sources_list` | `SELECT` | `parent` | Lists Sources in a given project and location. |
| `projects_locations_sources_create` | `INSERT` | `parent` | Creates a new Source in a given project and location. |
| `projects_locations_sources_delete` | `DELETE` | `name` | Deletes a single Source. |
| `projects_locations_sources_patch` | `EXEC` | `name` | Updates the parameters of a single Source. |
