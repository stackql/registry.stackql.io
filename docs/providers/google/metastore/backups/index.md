---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the backup, in the following form:projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id} |
| `description` | `string` | The description of the backup. |
| `state` | `string` | Output only. The current state of the backup. |
| `createTime` | `string` | Output only. The time when the backup was started. |
| `endTime` | `string` | Output only. The time when the backup finished creating. |
| `restoringServices` | `array` | Output only. Services that are restoring from the backup. |
| `serviceRevision` | `object` | A managed metastore service that serves metadata queries. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_backups_get` | `SELECT` | `name` | Gets details of a single backup. |
| `projects_locations_services_backups_list` | `SELECT` | `parent` | Lists backups in a service. |
| `projects_locations_services_backups_create` | `INSERT` | `parent` | Creates a new backup in a given project and location. |
| `projects_locations_services_backups_delete` | `DELETE` | `name` | Deletes a single backup. |
