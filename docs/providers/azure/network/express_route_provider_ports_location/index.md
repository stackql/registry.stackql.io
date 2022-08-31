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
| `location` | `string` | Resource location. |
| `portPairDescriptor` | `string` | The name of the port pair. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `portBandwidthInMbps` | `integer` | Bandwidth of the port in Mbps |
| `usedBandwidthInMbps` | `integer` | Used Bandwidth of the port in Mbps |
| `remainingBandwidthInMbps` | `integer` | Remaining Bandwidth of the port in Mbps |
| `secondaryAzurePort` | `string` | The name of the secondary port. |
| `overprovisionFactor` | `integer` | Overprovisioning factor for the port pair. |
| `primaryAzurePort` | `string` | The name of the primary port. |
| `tags` | `object` | Resource tags. |
| `peeringLocation` | `string` | The peering location of the port pair. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ExpressRouteProviderPortsLocation_List` | `SELECT` | `subscriptionId` |
