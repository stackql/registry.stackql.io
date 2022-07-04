---
title: machine_images
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_images
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
<tr><td><b>Name</b></td><td><code>machine_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.machine_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this machine image. The server defines this identifier. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `kind` | `string` | [Output Only] The resource type, which is always compute#machineImage for machine image. |
| `status` | `string` | [Output Only] The status of the machine image. One of the following values: INVALID, CREATING, READY, DELETING, and UPLOADING. |
| `creationTimestamp` | `string` | [Output Only] The creation timestamp for this machine image in RFC3339 text format. |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `savedDisks` | `array` | An array of Machine Image specific properties for disks attached to the source instance |
| `selfLink` | `string` | [Output Only] The URL for this machine image. The server defines this URL. |
| `sourceInstance` | `string` | The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance  |
| `storageLocations` | `array` | The regional or multi-regional Cloud Storage bucket location where the machine image is stored. |
| `totalStorageBytes` | `string` | [Output Only] Total size of the storage used by the machine image. |
| `machineImageEncryptionKey` | `object` |  |
| `instanceProperties` | `object` |  |
| `guestFlush` | `boolean` | [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process. |
| `sourceDiskEncryptionKeys` | `array` | [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key. |
| `sourceInstanceProperties` | `object` | DEPRECATED: Please use compute#instanceProperties instead. New properties will not be added to this field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `machineImages_get` | `SELECT` | `machineImage, project` | Returns the specified machine image. Gets a list of available machine images by making a list() request. |
| `machineImages_list` | `SELECT` | `project` | Retrieves a list of machine images that are contained within the specified project. |
| `machineImages_insert` | `INSERT` | `project` | Creates a machine image in the specified project using the data that is included in the request. If you are creating a new machine image to update an existing instance, your new machine image should use the same network or, if applicable, the same subnetwork as the original instance. |
| `machineImages_delete` | `DELETE` | `machineImage, project` | Deletes the specified machine image. Deleting a machine image is permanent and cannot be undone. |