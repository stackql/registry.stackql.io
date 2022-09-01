---
title: gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_image_versions
  - compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.gallery_image_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `publishingProfile` | `object` | The publishing profile of a gallery image Version. |
| `replicationStatus` | `object` | This is the replication status of the gallery image version. |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `storageProfile` | `object` | This is the storage profile of a Gallery Image Version. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GalleryImageVersions_ListByGalleryImage` | `SELECT` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | List gallery image versions in a gallery image definition. |
| `GalleryImageVersions_CreateOrUpdate` | `INSERT` | `galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery image version. |
| `GalleryImageVersions_Delete` | `DELETE` | `galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery image version. |
| `GalleryImageVersions_Get` | `EXEC` | `galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery image version. |
| `GalleryImageVersions_Update` | `EXEC` | `galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId` | Update a gallery image version. |
