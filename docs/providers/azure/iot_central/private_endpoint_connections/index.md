---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - iot_central
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
<tr><td><b>Id</b></td><td><code>azure.iot_central.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `groupIds` | `array` | The group ids for the private endpoint resource. |
| `privateEndpoint` | `object` | The private endpoint resource. |
| `privateLinkServiceConnectionState` | `object` | A collection of information about the state of the connection between service consumer and provider. |
| `provisioningState` | `string` | The current provisioning state. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get all private endpoint connections of a IoT Central Application. |
| `PrivateEndpointConnections_Create` | `INSERT` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Update a private endpoint connection. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Deletes a private endpoint connection from the IoT Central Application. |
| `PrivateEndpointConnections_Get` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Get the metadata of a private endpoint connection for the IoT Central Application. |