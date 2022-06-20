---
title: projects.hmacKeys
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
<tr><td><b>Name</b></td><td><code>projects.hmacKeys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.projects.hmacKeys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the HMAC key, including the Project ID and the Access ID. |
| `updated` | `string` | The last modification time of the HMAC key metadata in RFC 3339 format. |
| `projectId` | `string` | Project ID owning the service account to which the key authenticates. |
| `state` | `string` | The state of the key. Can be one of ACTIVE, INACTIVE, or DELETED. |
| `kind` | `string` | The kind of item this is. For HMAC Key metadata, this is always storage#hmacKeyMetadata. |
| `timeCreated` | `string` | The creation time of the HMAC key in RFC 3339 format. |
| `selfLink` | `string` | The link to this resource. |
| `accessId` | `string` | The ID of the HMAC Key. |
| `serviceAccountEmail` | `string` | The email address of the key's associated service account. |
| `etag` | `string` | HTTP 1.1 Entity tag for the HMAC key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessId, projectId` | Retrieves an HMAC key's metadata |
| `list` | `SELECT` | `projectId` | Retrieves a list of HMAC keys matching the criteria. |
| `create` | `INSERT` | `projectId, serviceAccountEmail` | Creates a new HMAC key for the specified service account. |
| `delete` | `DELETE` | `accessId, projectId` | Deletes an HMAC key. |
| `update` | `EXEC` | `accessId, projectId` | Updates the state of an HMAC key. See the HMAC Key resource descriptor for valid states. |
