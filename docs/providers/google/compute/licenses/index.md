---
title: licenses
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
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.licenses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. The name must be 1-63 characters long and comply with RFC1035. |
| `description` | `string` | An optional textual description of the resource; provided by the client when the resource is created. |
| `chargesUseFee` | `boolean` | [Output Only] Deprecated. This field no longer reflects whether a license charges a usage fee. |
| `transferable` | `boolean` | If false, licenses will not be copied from the source resource when creating an image from a disk, disk from snapshot, or snapshot from disk. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#license for licenses. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `resourceRequirements` | `object` |  |
| `licenseCode` | `string` | [Output Only] The unique code used to attach this license to images, snapshots, and disks. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `license, project` | Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| `list` | `SELECT` | `project` | Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud or windows-cloud. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| `insert` | `INSERT` | `project` | Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| `delete` | `DELETE` | `license, project` | Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| `getIamPolicy` | `EXEC` | `project, resource` | Gets the access control policy for a resource. May be empty if no such policy or resource exists. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| `setIamPolicy` | `EXEC` | `project, resource` | Sets the access control policy on the specified resource. Replaces any existing policy. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |
| `testIamPermissions` | `EXEC` | `project, resource` | Returns permissions that a caller has on the specified resource. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.  |