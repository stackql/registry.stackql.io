---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - groups
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The Group name. |
| `description` | `string` | User-provided description of the group. |
| `createTime` | `string` | Output only. The create time timestamp. |
| `displayName` | `string` | Display name is a user defined name for this group which can be updated. |
| `updateTime` | `string` | Output only. The update time timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_groups_get` | `SELECT` | `name` | Gets details of a single Group. |
| `projects_locations_groups_list` | `SELECT` | `parent` | Lists Groups in a given project and location. |
| `projects_locations_groups_create` | `INSERT` | `parent` | Creates a new Group in a given project and location. |
| `projects_locations_groups_delete` | `DELETE` | `name` | Deletes a single Group. |
| `projects_locations_groups_patch` | `EXEC` | `name` | Updates the parameters of a single Group. |
