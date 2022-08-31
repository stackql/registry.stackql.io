---
title: inbound_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_endpoints
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>inbound_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.inbound_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `provisioningState` | `string` | The current provisioning state of the resource. |
| `resourceGuid` | `string` | The Guid property of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | ETag of the inbound endpoint. |
| `ipConfigurations` | `array` | IP configurations for the inbound endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InboundEndpoints_List` | `SELECT` | `dnsResolverName, resourceGroupName, subscriptionId` | Lists inbound endpoints for a DNS resolver. |
| `InboundEndpoints_CreateOrUpdate` | `INSERT` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Creates or updates an inbound endpoint for a DNS resolver. |
| `InboundEndpoints_Delete` | `DELETE` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Deletes an inbound endpoint for a DNS resolver. WARNING: This operation cannot be undone. |
| `InboundEndpoints_Get` | `EXEC` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Gets properties of an inbound endpoint for a DNS resolver. |
| `InboundEndpoints_Update` | `EXEC` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Updates an inbound endpoint for a DNS resolver. |
