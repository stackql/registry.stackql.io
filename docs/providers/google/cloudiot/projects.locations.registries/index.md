---
title: projects.locations.registries
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
<tr><td><b>Name</b></td><td><code>projects.locations.registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudiot.projects.locations.registries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deviceRegistries` | `array` | The registries that matched the query. |
| `nextPageToken` | `string` | If not empty, indicates that there may be more registries that match the request; this value should be passed in a new `ListDeviceRegistriesRequest`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, registriesId` | Gets details about a device. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists device registries. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a device registry that contains devices. |
| `delete` | `DELETE` | `locationsId, projectsId, registriesId` | Deletes a device. |
| `bindDeviceToGateway` | `EXEC` | `locationsId, projectsId, registriesId` | Associates the device with the gateway. |
| `getIamPolicy` | `EXEC` | `locationsId, projectsId, registriesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `patch` | `EXEC` | `locationsId, projectsId, registriesId` | Updates a device. |
| `setIamPolicy` | `EXEC` | `locationsId, projectsId, registriesId` | Sets the access control policy on the specified resource. Replaces any existing policy. |
| `testIamPermissions` | `EXEC` | `locationsId, projectsId, registriesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error. |
| `unbindDeviceFromGateway` | `EXEC` | `locationsId, projectsId, registriesId` | Deletes the association between the device and the gateway. |
