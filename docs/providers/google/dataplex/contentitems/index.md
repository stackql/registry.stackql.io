---
title: contentitems
hide_title: false
hide_table_of_contents: false
keywords:
  - contentitems
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
<tr><td><b>Name</b></td><td><code>contentitems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.contentitems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id} |
| `description` | `string` | Optional. Description of the content. |
| `createTime` | `string` | Output only. Content creation time. |
| `updateTime` | `string` | Output only. The time when the content was last updated. |
| `path` | `string` | Required. The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes. |
| `labels` | `object` | Optional. User defined labels for the content. |
| `dataText` | `string` | Required. Content data in string format. |
| `notebook` | `object` | Configuration for Notebook content. |
| `sqlScript` | `object` | Configuration for the Sql Script content. |
| `uid` | `string` | Output only. System generated globally unique ID for the content. This ID will be different if the content is deleted and re-created with the same name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_contentitems_get` | `SELECT` | `name` | Get a content resource. |
| `projects_locations_lakes_contentitems_list` | `SELECT` | `parent` | List content. |
| `projects_locations_lakes_contentitems_create` | `INSERT` | `parent` | Create a content. |
| `projects_locations_lakes_contentitems_delete` | `DELETE` | `name` | Delete a content. |
| `projects_locations_lakes_contentitems_patch` | `EXEC` | `name` | Update a content. Only supports full resource update. |
