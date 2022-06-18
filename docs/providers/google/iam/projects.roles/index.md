---
title: projects.roles
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>projects.roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.projects.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `roles` | `array` | The Roles defined on this resource. |
| `nextPageToken` | `string` | To retrieve the next page of results, set `ListRolesRequest.page_token` to this value. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `projectsId, rolesId` | Gets the definition of a Role. |
| `list` | `SELECT` | `projectsId` | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| `create` | `INSERT` | `projectsId` | Creates a new custom Role. |
| `delete` | `DELETE` | `projectsId, rolesId` | Deletes a ServiceAccountKey. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key. |
| `patch` | `EXEC` | `projectsId, rolesId` | Patches a ServiceAccount. |
| `undelete` | `EXEC` | `projectsId, rolesId` | Restores a deleted ServiceAccount. **Important:** It is not always possible to restore a deleted service account. Use this method only as a last resort. After you delete a service account, IAM permanently removes the service account 30 days later. There is no way to restore a deleted service account that has been permanently removed. |
