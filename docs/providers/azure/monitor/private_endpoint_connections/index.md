---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - monitor
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
<tr><td><b>Id</b></td><td><code>azure.monitor.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `privateEndpoint` | `object` | The Private Endpoint resource. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `type` | `string` | Azure resource type |
| `location` | `string` | Resource location |
| `privateLinkServiceConnectionState` | `object` | A collection of information about the state of the connection between service consumer and provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_ListByPrivateLinkScope` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` | Gets all private endpoint connections on a private link scope. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId` | Deletes a private endpoint connection with a given name. |
| `PrivateEndpointConnections_Get` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId` | Gets a private endpoint connection. |
