---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - dns
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
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns.zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `maxNumberOfRecordSets` | `integer` | The maximum number of record sets that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. |
| `type` | `string` | Resource type. |
| `etag` | `string` | The etag of the zone. |
| `maxNumberOfRecordsPerRecordSet` | `integer` | The maximum number of records per record set that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. |
| `numberOfRecordSets` | `integer` | The current number of record sets in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. |
| `location` | `string` | Resource location. |
| `tags` | `object` | Resource tags. |
| `nameServers` | `array` | The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored. |
| `zoneType` | `string` | The type of this DNS zone (Public or Private). |
| `resolutionVirtualNetworks` | `array` | A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private. |
| `registrationVirtualNetworks` | `array` | A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Zones_List` | `SELECT` | `subscriptionId` | Lists the DNS zones in all resource groups in a subscription. |
| `Zones_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the DNS zones within a resource group. |
| `Zones_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, zoneName` | Creates or updates a DNS zone. Does not modify DNS records within the zone. |
| `Zones_Delete` | `DELETE` | `resourceGroupName, subscriptionId, zoneName` | Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. |
| `Zones_Get` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` | Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone. |
| `Zones_Update` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` | Updates a DNS zone. Does not modify DNS records within the zone. |
