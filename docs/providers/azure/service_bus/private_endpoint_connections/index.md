---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - service_bus
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
<tr><td><b>Id</b></td><td><code>azure.service_bus.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
| `privateEndpoint` | `object` | PrivateEndpoint information. |
| `privateLinkServiceConnectionState` | `object` | ConnectionState information. |
| `provisioningState` | `string` | Provisioning state of the Private Endpoint Connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_List` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets the available PrivateEndpointConnections within a namespace. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `namespaceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Creates or updates PrivateEndpointConnections of service namespace. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `namespaceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes an existing Private Endpoint Connection. |
| `PrivateEndpointConnections_Get` | `EXEC` | `namespaceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets a description for the specified Private Endpoint Connection. |