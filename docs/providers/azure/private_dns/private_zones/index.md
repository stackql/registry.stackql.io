---
title: private_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - private_zones
  - private_dns
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
<tr><td><b>Name</b></td><td><code>private_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.private_dns.private_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The ETag of the zone. |
| `location` | `string` | The Azure Region where the resource lives |
| `internalId` | `string` | Private zone internal Id |
| `maxNumberOfRecordSets` | `integer` | The maximum number of record sets that can be created in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |
| `numberOfVirtualNetworkLinks` | `integer` | The current number of virtual networks that are linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |
| `numberOfVirtualNetworkLinksWithRegistration` | `integer` | The current number of virtual networks that are linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored. |
| `maxNumberOfVirtualNetworkLinks` | `integer` | The maximum number of virtual networks that can be linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |
| `maxNumberOfVirtualNetworkLinksWithRegistration` | `integer` | The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The provisioning state of the resource. This is a read-only property and any attempt to set this value will be ignored. |
| `numberOfRecordSets` | `integer` | The current number of record sets in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateZones_List` | `SELECT` | `subscriptionId` | Lists the Private DNS zones in all resource groups in a subscription. |
| `PrivateZones_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Private DNS zones within a resource group. |
| `PrivateZones_CreateOrUpdate` | `INSERT` | `privateZoneName, resourceGroupName, subscriptionId` | Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone. |
| `PrivateZones_Delete` | `DELETE` | `privateZoneName, resourceGroupName, subscriptionId` | Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed. |
| `PrivateZones_Get` | `EXEC` | `privateZoneName, resourceGroupName, subscriptionId` | Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone. |
| `PrivateZones_Update` | `EXEC` | `privateZoneName, resourceGroupName, subscriptionId` | Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone. |
