---
title: express_route_provider_ports_location
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_provider_ports_location
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
<tr><td><b>Name</b></td><td><code>express_route_provider_ports_location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_provider_ports_location</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `peeringLocation` | `string` | The peering location of the port pair. |
| `overprovisionFactor` | `integer` | Overprovisioning factor for the port pair. |
| `remainingBandwidthInMbps` | `integer` | Remaining Bandwidth of the port in Mbps |
| `location` | `string` | Resource location. |
| `secondaryAzurePort` | `string` | The name of the secondary port. |
| `type` | `string` | Resource type. |
| `usedBandwidthInMbps` | `integer` | Used Bandwidth of the port in Mbps |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `primaryAzurePort` | `string` | The name of the primary port. |
| `portBandwidthInMbps` | `integer` | Bandwidth of the port in Mbps |
| `tags` | `object` | Resource tags. |
| `portPairDescriptor` | `string` | The name of the port pair. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ExpressRouteProviderPortsLocation_List` | `SELECT` | `subscriptionId` |
