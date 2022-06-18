---
title: projects.locations.workloadIdentityPools.providers
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
<tr><td><b>Name</b></td><td><code>projects.locations.workloadIdentityPools.providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.projects.locations.workloadIdentityPools.providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `workloadIdentityPoolProviders` | `array` | A list of providers. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Gets the definition of a Role. |
| `list` | `SELECT` | `locationsId, projectsId, workloadIdentityPoolsId` | Lists all non-deleted WorkloadIdentityPoolProviders in a WorkloadIdentityPool. If `show_deleted` is set to `true`, then deleted providers are also listed. |
| `create` | `INSERT` | `locationsId, projectsId, workloadIdentityPoolsId` | Creates a new WorkloadIdentityPoolProvider in a WorkloadIdentityPool. You cannot reuse the name of a deleted provider until 30 days after deletion. |
| `delete` | `DELETE` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Deletes a ServiceAccountKey. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key. |
| `patch` | `EXEC` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Patches a ServiceAccount. |
| `undelete` | `EXEC` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Restores a deleted ServiceAccount. **Important:** It is not always possible to restore a deleted service account. Use this method only as a last resort. After you delete a service account, IAM permanently removes the service account 30 days later. There is no way to restore a deleted service account that has been permanently removed. |
