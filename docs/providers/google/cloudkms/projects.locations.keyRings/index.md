---
title: projects.locations.keyRings
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
<tr><td><b>Name</b></td><td><code>projects.locations.keyRings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.projects.locations.keyRings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `keyRings` | `array` | The list of KeyRings. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListKeyRingsRequest.page_token to retrieve the next page of results. |
| `totalSize` | `integer` | The total number of KeyRings that matched the query. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `keyRingsId, locationsId, projectsId` | Returns metadata for a given ImportJob. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists KeyRings. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new KeyRing in a given Project and Location. |
| `getIamPolicy` | `EXEC` | `keyRingsId, locationsId, projectsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `setIamPolicy` | `EXEC` | `keyRingsId, locationsId, projectsId` | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| `testIamPermissions` | `EXEC` | `keyRingsId, locationsId, projectsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
