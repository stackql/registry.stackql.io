---
title: virtual_appliance_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_skus
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_appliance_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_appliance_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `availableScaleUnits` | `array` | The list of scale units available. |
| `tags` | `object` | Resource tags. |
| `availableVersions` | `array` | Available Network Virtual Appliance versions. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `vendor` | `string` | Network Virtual Appliance Sku vendor. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualApplianceSkus_List` | `SELECT` | `subscriptionId` | List all SKUs available for a virtual appliance. |
| `VirtualApplianceSkus_Get` | `EXEC` | `skuName, subscriptionId` | Retrieves a single available sku for network virtual appliance. |
