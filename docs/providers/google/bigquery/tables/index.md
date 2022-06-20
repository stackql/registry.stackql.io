---
title: tables
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
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalItems` | `integer` | The total number of tables in the dataset. |
| `etag` | `string` | A hash of this page of results. |
| `kind` | `string` | The type of list. |
| `nextPageToken` | `string` | A token to request the next page of results. |
| `tables` | `array` | Tables in the requested dataset. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetId, projectId, tableId` | Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table. |
| `list` | `SELECT` | `datasetId, projectId` | Lists all tables in the specified dataset. Requires the READER dataset role. |
| `insert` | `INSERT` | `datasetId, projectId, data__tableReference` | Creates a new, empty table in the dataset. |
| `delete` | `DELETE` | `datasetId, projectId, tableId` | Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted. |
| `getIamPolicy` | `EXEC` | `datasetsId, projectsId, tablesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `patch` | `EXEC` | `datasetId, projectId, tableId, data__tableReference` | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics. |
| `setIamPolicy` | `EXEC` | `datasetsId, projectsId, tablesId` | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| `testIamPermissions` | `EXEC` | `datasetsId, projectsId, tablesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
| `update` | `EXEC` | `datasetId, projectId, tableId, data__tableReference` | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. |
