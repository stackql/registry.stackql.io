---
title: shared_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_image_versions
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
<tr><td><b>Name</b></td><td><code>shared_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.shared_gallery_image_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `publishedDate` | `string` | The published date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable. |
| `storageProfile` | `object` | This is the storage profile of a Gallery Image Version. |
| `endOfLifeDate` | `string` | The end of life date of the gallery image version Definition. This property can be used for decommissioning purposes. This property is updatable. |
| `excludeFromLatest` | `boolean` | If set to true, Virtual Machines deployed from the latest version of the Image Definition won't use this Image Version. |
| `identifier` | `object` | The identifier information of shared gallery. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SharedGalleryImageVersions_List` | `SELECT` | `galleryImageName, galleryUniqueName, location, subscriptionId` | List shared gallery image versions by subscription id or tenant id. |
| `SharedGalleryImageVersions_Get` | `EXEC` | `galleryImageName, galleryImageVersionName, galleryUniqueName, location, subscriptionId` | Get a shared gallery image version by subscription id or tenant id. |
