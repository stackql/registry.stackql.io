---
title: gallery_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_applications
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
<tr><td><b>Name</b></td><td><code>gallery_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.gallery_applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `description` | `string` | The description of this gallery Application Definition resource. This property is updatable. |
| `supportedOSType` | `string` | This property allows you to specify the supported type of the OS that application is built for. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |
| `tags` | `object` | Resource tags |
| `privacyStatementUri` | `string` | The privacy statement uri. |
| `eula` | `string` | The Eula agreement for the gallery Application Definition. |
| `type` | `string` | Resource type |
| `endOfLifeDate` | `string` | The end of life date of the gallery Application Definition. This property can be used for decommissioning purposes. This property is updatable. |
| `location` | `string` | Resource location |
| `releaseNoteUri` | `string` | The release note uri. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GalleryApplications_ListByGallery` | `SELECT` | `galleryName, resourceGroupName, subscriptionId` | List gallery Application Definitions in a gallery. |
| `GalleryApplications_CreateOrUpdate` | `INSERT` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery Application Definition. |
| `GalleryApplications_Delete` | `DELETE` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery Application. |
| `GalleryApplications_Get` | `EXEC` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery Application Definition. |
| `GalleryApplications_Update` | `EXEC` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Update a gallery Application Definition. |
