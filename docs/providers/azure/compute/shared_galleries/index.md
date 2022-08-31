---
title: shared_galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_galleries
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
<tr><td><b>Name</b></td><td><code>shared_galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.shared_galleries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `array` | A list of shared galleries. |
| `nextLink` | `string` | The uri to fetch the next page of shared galleries. Call ListNext() with this to fetch the next page of shared galleries. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SharedGalleries_List` | `SELECT` | `location, subscriptionId` | List shared galleries by subscription id or tenant id. |
| `SharedGalleries_Get` | `EXEC` | `galleryUniqueName, location, subscriptionId` | Get a shared gallery by subscription id or tenant id. |
