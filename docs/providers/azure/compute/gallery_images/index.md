---
title: gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_images
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
<tr><td><b>Name</b></td><td><code>gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.gallery_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `description` | `string` | The description of this gallery image definition resource. This property is updatable. |
| `osType` | `string` | This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |
| `releaseNoteUri` | `string` | The release note uri. |
| `osState` | `string` | This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'. |
| `type` | `string` | Resource type |
| `recommended` | `object` | The properties describe the recommended machine configuration for this Image Definition. These properties are updatable. |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |
| `tags` | `object` | Resource tags |
| `features` | `array` | A list of gallery image features. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `endOfLifeDate` | `string` | The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable. |
| `identifier` | `object` | This is the gallery image definition identifier. |
| `location` | `string` | Resource location |
| `disallowed` | `object` | Describes the disallowed disk types. |
| `eula` | `string` | The Eula agreement for the gallery image definition. |
| `purchasePlan` | `object` | Describes the gallery image definition purchase plan. This is used by marketplace images. |
| `privacyStatementUri` | `string` | The privacy statement uri. |
| `architecture` | `string` | The architecture of the image. Applicable to OS disks only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GalleryImages_ListByGallery` | `SELECT` | `galleryName, resourceGroupName, subscriptionId` | List gallery image definitions in a gallery. |
| `GalleryImages_CreateOrUpdate` | `INSERT` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery image definition. |
| `GalleryImages_Delete` | `DELETE` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery image. |
| `GalleryImages_Get` | `EXEC` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery image definition. |
| `GalleryImages_Update` | `EXEC` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Update a gallery image definition. |
