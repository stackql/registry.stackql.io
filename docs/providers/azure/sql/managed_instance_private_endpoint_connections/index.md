---
title: managed_instance_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_private_endpoint_connections
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_instance_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | State of the Private Endpoint Connection. |
| `privateEndpoint` | `object` |  |
| `privateLinkServiceConnectionState` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstancePrivateEndpointConnections_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets all private endpoint connections on a server. |
| `ManagedInstancePrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `ManagedInstancePrivateEndpointConnections_Delete` | `DELETE` | `managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection with a given name. |
| `ManagedInstancePrivateEndpointConnections_Get` | `EXEC` | `managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets a private endpoint connection. |
