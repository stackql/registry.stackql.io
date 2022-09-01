---
title: community_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_images
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
<tr><td><b>Name</b></td><td><code>community_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.community_gallery_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name |
| `endOfLifeDate` | `string` | The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable. |
| `identifier` | `object` | The identifier information of community gallery. |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine. Applicable to OS disks only. |
| `osType` | `string` | This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |
| `recommended` | `object` | The properties describe the recommended machine configuration for this Image Definition. These properties are updatable. |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `architecture` | `string` | The architecture of the image. Applicable to OS disks only. |
| `purchasePlan` | `object` | Describes the gallery image definition purchase plan. This is used by marketplace images. |
| `disallowed` | `object` | Describes the disallowed disk types. |
| `features` | `array` | A list of gallery image features. |
| `privacyStatementUri` | `string` | Privacy statement uri for the current community gallery image. |
| `osState` | `string` | This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'. |
| `eula` | `string` | End-user license agreement for the current community gallery image. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CommunityGalleryImages_List` | `SELECT` | `location, publicGalleryName, subscriptionId` | List community gallery images inside a gallery. |
| `CommunityGalleryImages_Get` | `EXEC` | `galleryImageName, location, publicGalleryName, subscriptionId` | Get a community gallery image. |
