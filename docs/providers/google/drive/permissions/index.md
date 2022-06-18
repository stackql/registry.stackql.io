---
title: permissions
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
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | The page token for the next page of permissions. This field will be absent if the end of the permissions list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
| `permissions` | `array` | The list of permissions. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#permissionList". |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `fileId, permissionId` | Gets a permission by ID. |
| `list` | `SELECT` | `fileId` | Lists a file's or shared drive's permissions. |
| `create` | `INSERT` | `fileId` | Creates a permission for a file or shared drive. |
| `delete` | `DELETE` | `fileId, permissionId` | Deletes a permission. |
| `update` | `EXEC` | `fileId, permissionId` | Updates a permission with patch semantics. |
