---
title: projects.serviceAccounts.keys
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
<tr><td><b>Name</b></td><td><code>projects.serviceAccounts.keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.projects.serviceAccounts.keys</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `keysId, projectsId, serviceAccountsId` | Gets the definition of a Role. |
| `list` | `SELECT` | `projectsId, serviceAccountsId` | Lists every ServiceAccountKey for a service account. |
| `create` | `INSERT` | `projectsId, serviceAccountsId` | Creates a ServiceAccountKey. |
| `delete` | `DELETE` | `keysId, projectsId, serviceAccountsId` | Deletes a ServiceAccountKey. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key. |
| `disable` | `EXEC` | `keysId, projectsId, serviceAccountsId` | Disable a ServiceAccountKey. A disabled service account key can be enabled through EnableServiceAccountKey. |
| `enable` | `EXEC` | `keysId, projectsId, serviceAccountsId` | Enable a ServiceAccountKey. |
| `upload` | `EXEC` | `projectsId, serviceAccountsId` | Creates a ServiceAccountKey, using a public key that you provide. |
