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
<tr><td><b>Id</b></td><td><code>google.file.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the backup, in the format `projects/{project_number}/locations/{location_id}/backups/{backup_id}`. |
| `description` | `string` | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected. |
| `capacityGb` | `string` | Output only. Capacity of the source file share when the backup was created. |
| `labels` | `object` | Resource labels to represent user provided metadata. |
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `sourceInstanceTier` | `string` | Output only. The service tier of the source Cloud Filestore instance that this backup is created from. |
| `sourceFileShare` | `string` | Name of the file share in the source Cloud Filestore instance that the backup is created from. |
| `state` | `string` | Output only. The backup state. |
| `storageBytes` | `string` | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion. |
| `downloadBytes` | `string` | Output only. Amount of bytes that will be downloaded if the backup is restored. This may be different than storage bytes, since sequential backups of the same disk will share storage. |
| `createTime` | `string` | Output only. The time when the backup was created. |
| `sourceInstance` | `string` | The resource name of the source Cloud Filestore instance, in the format `projects/{project_number}/locations/{location_id}/instances/{instance_id}`, used to create this backup. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_backups_get` | `SELECT` | `name` | Gets the details of a specific backup. |
| `projects_locations_backups_list` | `SELECT` | `parent` | Lists all backups in a project for either a specified location or for all locations. |
| `projects_locations_backups_create` | `INSERT` | `parent` | Creates a backup. |
| `projects_locations_backups_delete` | `DELETE` | `name` | Deletes a backup. |
| `projects_locations_backups_patch` | `EXEC` | `name` | Updates the settings of a specific backup. |
