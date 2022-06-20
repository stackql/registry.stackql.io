---
title: projects.serviceAccounts
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
<tr><td><b>Name</b></td><td><code>projects.serviceAccounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.projects.serviceAccounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accounts` | `array` | The list of matching service accounts. |
| `nextPageToken` | `string` | To retrieve the next page of results, set ListServiceAccountsRequest.page_token to this value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, serviceAccountsId` | Gets the definition of a Role. |
| `list` | `SELECT` | `projectsId` | Lists every ServiceAccount that belongs to a specific project. |
| `create` | `INSERT` | `projectsId` | Creates a ServiceAccount. |
| `delete` | `DELETE` | `projectsId, serviceAccountsId` | Deletes a ServiceAccountKey. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key. |
| `disable` | `EXEC` | `projectsId, serviceAccountsId` | Disable a ServiceAccountKey. A disabled service account key can be enabled through EnableServiceAccountKey. |
| `enable` | `EXEC` | `projectsId, serviceAccountsId` | Enable a ServiceAccountKey. |
| `getIamPolicy` | `EXEC` | `projectsId, serviceAccountsId` | Gets the IAM policy that is attached to a ServiceAccount. This IAM policy specifies which principals have access to the service account. This method does not tell you whether the service account has been granted any roles on other resources. To check whether a service account has role grants on a resource, use the `getIamPolicy` method for that resource. For example, to view the role grants for a project, call the Resource Manager API's [`projects.getIamPolicy`](https://cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy) method. |
| `patch` | `EXEC` | `projectsId, serviceAccountsId` | Patches a ServiceAccount. |
| `setIamPolicy` | `EXEC` | `projectsId, serviceAccountsId` | Sets the IAM policy that is attached to a ServiceAccount. Use this method to grant or revoke access to the service account. For example, you could grant a principal the ability to impersonate the service account. This method does not enable the service account to access other resources. To grant roles to a service account on a resource, follow these steps: 1. Call the resource's `getIamPolicy` method to get its current IAM policy. 2. Edit the policy so that it binds the service account to an IAM role for the resource. 3. Call the resource's `setIamPolicy` method to update its IAM policy. For detailed instructions, see [Manage access to project, folders, and organizations](https://cloud.google.com/iam/help/service-accounts/granting-access-to-service-accounts) or [Manage access to other resources](https://cloud.google.com/iam/help/access/manage-other-resources). |
| `signBlob` | `EXEC` | `projectsId, serviceAccountsId` | **Note:** This method is deprecated. Use the [`signBlob`](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signBlob) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions. Signs a blob using the system-managed private key for a ServiceAccount. |
| `signJwt` | `EXEC` | `projectsId, serviceAccountsId` | **Note:** This method is deprecated. Use the [`signJwt`](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signJwt) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions. Signs a JSON Web Token (JWT) using the system-managed private key for a ServiceAccount. |
| `testIamPermissions` | `EXEC` | `projectsId, serviceAccountsId` | Tests whether the caller has the specified permissions on a ServiceAccount. |
| `undelete` | `EXEC` | `projectsId, serviceAccountsId` | Restores a deleted ServiceAccount. **Important:** It is not always possible to restore a deleted service account. Use this method only as a last resort. After you delete a service account, IAM permanently removes the service account 30 days later. There is no way to restore a deleted service account that has been permanently removed. |
| `update` | `EXEC` | `projectsId, serviceAccountsId` | **Note:** We are in the process of deprecating this method. Use PatchServiceAccount instead. Updates a ServiceAccount. You can update only the `display_name` and `description` fields. |
