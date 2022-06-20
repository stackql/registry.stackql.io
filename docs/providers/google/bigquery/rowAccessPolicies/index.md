---
title: rowAccessPolicies
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
<tr><td><b>Name</b></td><td><code>rowAccessPolicies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.rowAccessPolicies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rowAccessPolicies` | `array` | Row access policies on the requested table. |
| `nextPageToken` | `string` | A token to request the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `datasetsId, projectsId, tablesId` | Lists all row access policies on the specified table. |
| `getIamPolicy` | `EXEC` | `datasetsId, projectsId, rowAccessPoliciesId, tablesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `setIamPolicy` | `EXEC` | `datasetsId, projectsId, rowAccessPoliciesId, tablesId` | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| `testIamPermissions` | `EXEC` | `datasetsId, projectsId, rowAccessPoliciesId, tablesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |