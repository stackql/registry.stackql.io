---
title: projects.locations.registries.groups
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
<tr><td><b>Name</b></td><td><code>projects.locations.registries.groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudiot.projects.locations.registries.groups</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `getIamPolicy` | `EXEC` | `groupsId, locationsId, projectsId, registriesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `setIamPolicy` | `EXEC` | `groupsId, locationsId, projectsId, registriesId` | Sets the access control policy on the specified resource. Replaces any existing policy. |
| `testIamPermissions` | `EXEC` | `groupsId, locationsId, projectsId, registriesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error. |
