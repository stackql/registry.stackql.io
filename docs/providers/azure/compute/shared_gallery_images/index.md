---
title: shared_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_images
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
<tr><td><b>Name</b></td><td><code>shared_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.shared_gallery_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endOfLifeDate` | `string` | The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable. |
| `architecture` | `string` | The architecture of the image. Applicable to OS disks only. |
| `features` | `array` | A list of gallery image features. |
| `disallowed` | `object` | Describes the disallowed disk types. |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |
| `identifier` | `object` | The identifier information of shared gallery. |
| `osState` | `string` | This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'. |
| `recommended` | `object` | The properties describe the recommended machine configuration for this Image Definition. These properties are updatable. |
| `purchasePlan` | `object` | Describes the gallery image definition purchase plan. This is used by marketplace images. |
| `osType` | `string` | This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SharedGalleryImages_List` | `SELECT` | `galleryUniqueName, location, subscriptionId` | List shared gallery images by subscription id or tenant id. |
| `SharedGalleryImages_Get` | `EXEC` | `galleryImageName, galleryUniqueName, location, subscriptionId` | Get a shared gallery image by subscription id or tenant id. |
