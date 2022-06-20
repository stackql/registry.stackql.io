---
title: projects.locations.connections
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
<tr><td><b>Name</b></td><td><code>projects.locations.connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryconnection.projects.locations.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Next page token. |
| `connections` | `array` | List of connections. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionsId, locationsId, projectsId` | Returns specified connection. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns a list of connections in the given project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new connection. |
| `delete` | `DELETE` | `connectionsId, locationsId, projectsId` | Deletes connection and associated credential. |
| `getIamPolicy` | `EXEC` | `connectionsId, locationsId, projectsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `patch` | `EXEC` | `connectionsId, locationsId, projectsId` | Sets the credential for the specified connection. |
| `setIamPolicy` | `EXEC` | `connectionsId, locationsId, projectsId` | Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors. |
| `testIamPermissions` | `EXEC` | `connectionsId, locationsId, projectsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
| `updateCredential` | `EXEC` | `connectionsId, locationsId, projectsId` | Sets the credential for the specified connection. |
