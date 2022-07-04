---
title: restores
hide_title: false
hide_table_of_contents: false
keywords:
  - restores
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
<tr><td><b>Name</b></td><td><code>restores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.restores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the Restore resource. Format: projects/*/locations/*/restorePlans/*/restores/* |
| `description` | `string` | User specified descriptive string for this Restore. |
| `cluster` | `string` | Output only. The target cluster into which this Restore will restore data. Valid formats: - projects/*/locations/*/clusters/* - projects/*/zones/*/clusters/* Inherited from parent RestorePlan's cluster value. |
| `resourcesExcludedCount` | `integer` | Output only. Number of resources excluded during the restore execution. |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
| `volumesRestoredCount` | `integer` | Output only. Number of volumes restored during the restore execution. |
| `resourcesRestoredCount` | `integer` | Output only. Number of resources restored during the restore execution. |
| `updateTime` | `string` | Output only. The timestamp when this Restore resource was last updated. |
| `completeTime` | `string` | Output only. Timestamp of when the restore operation completed. |
| `createTime` | `string` | Output only. The timestamp when this Restore resource was created. |
| `restoreConfig` | `object` | Configuration of a restore. Next id: 9 |
| `stateReason` | `string` | Output only. Human-readable description of why the Restore is in its current state. |
| `labels` | `object` | A set of custom labels supplied by user. |
| `backup` | `string` | Required. Immutable. A reference to the Backup used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's backup_plan. Format: projects/*/locations/*/backupPlans/*/backups/*. |
| `resourcesFailedCount` | `integer` | Output only. Number of resources that failed to be restored during the restore execution. |
| `state` | `string` | Output only. The current state of the Restore. |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestore`, and systems are expected to put that etag in the request to `UpdateRestore` or `DeleteRestore` to ensure that their change will be applied to the same version of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_restorePlans_restores_get` | `SELECT` | `name` | Retrieves the details of a single Restore. |
| `projects_locations_restorePlans_restores_list` | `SELECT` | `parent` | Lists the Restores for a given RestorePlan. |
| `projects_locations_restorePlans_restores_create` | `INSERT` | `parent` | Creates a new Restore for the given RestorePlan. |
| `projects_locations_restorePlans_restores_delete` | `DELETE` | `name` | Deletes an existing Restore. |
| `projects_locations_restorePlans_restores_patch` | `EXEC` | `name` | Update a Restore. |