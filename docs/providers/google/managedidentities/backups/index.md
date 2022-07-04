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
<tr><td><b>Id</b></td><td><code>google.managedidentities.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique name of the Backup in the form of `projects/{project_id}/locations/global/domains/{domain_name}/backups/{name}` |
| `updateTime` | `string` | Output only. Last update time. |
| `createTime` | `string` | Output only. The time the backups was created. |
| `labels` | `object` | Optional. Resource labels to represent user provided metadata. |
| `state` | `string` | Output only. The current state of the backup. |
| `statusMessage` | `string` | Output only. Additional information about the current status of this backup, if available. |
| `type` | `string` | Output only. Indicates whether it’s an on-demand backup or scheduled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_domains_backups_get` | `SELECT` | `name` | Gets details of a single Backup. |
| `projects_locations_global_domains_backups_list` | `SELECT` | `parent` | Lists Backup in a given project. |
| `projects_locations_global_domains_backups_create` | `INSERT` | `parent` | Creates a Backup for a domain. |
| `projects_locations_global_domains_backups_delete` | `DELETE` | `name` | Deletes identified Backup. |
| `projects_locations_global_domains_backups_patch` | `EXEC` | `name` | Updates the labels for specified Backup. |
