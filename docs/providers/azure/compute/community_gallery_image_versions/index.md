---
title: community_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_image_versions
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
<tr><td><b>Name</b></td><td><code>community_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.community_gallery_image_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name |
| `endOfLifeDate` | `string` | The end of life date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable. |
| `excludeFromLatest` | `boolean` | If set to true, Virtual Machines deployed from the latest version of the Image Definition won't use this Image Version. |
| `identifier` | `object` | The identifier information of community gallery. |
| `location` | `string` | Resource location |
| `publishedDate` | `string` | The published date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable. |
| `storageProfile` | `object` | This is the storage profile of a Gallery Image Version. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CommunityGalleryImageVersions_List` | `SELECT` | `galleryImageName, location, publicGalleryName, subscriptionId` | List community gallery image versions inside an image. |
| `CommunityGalleryImageVersions_Get` | `EXEC` | `galleryImageName, galleryImageVersionName, location, publicGalleryName, subscriptionId` | Get a community gallery image version. |
