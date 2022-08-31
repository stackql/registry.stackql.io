---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - event_grid
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `provisioningState` | `string` | Provisioning state of the Private Endpoint Connection. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `groupIds` | `array` | GroupIds from the private link service resource. |
| `privateEndpoint` | `object` | PrivateEndpoint information. |
| `privateLinkServiceConnectionState` | `object` | ConnectionState information. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_ListByResource` | `SELECT` | `parentName, parentType, resourceGroupName, subscriptionId` | Get all private endpoint connections under a topic, domain, or partner namespace. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Delete a specific private endpoint connection under a topic, domain, or partner namespace. |
| `PrivateEndpointConnections_Get` | `EXEC` | `parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Get a specific private endpoint connection under a topic, domain, or partner namespace. |
| `PrivateEndpointConnections_Update` | `EXEC` | `parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Update a specific private endpoint connection under a topic, domain or partner namespace. |
