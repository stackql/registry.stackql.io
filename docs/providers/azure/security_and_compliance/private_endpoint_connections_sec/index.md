---
title: private_endpoint_connections_sec
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_sec
  - security_and_compliance
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_sec</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_and_compliance.private_endpoint_connections_sec</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `provisioningState` | `string` | The current provisioning state. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `privateEndpoint` | `object` | The Private Endpoint resource. |
| `privateLinkServiceConnectionState` | `object` | A collection of information about the state of the connection between service consumer and provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnectionsSec_ListByService` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Lists all private endpoint connections for a service. |
| `PrivateEndpointConnectionsSec_CreateOrUpdate` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Update the state of the specified private endpoint connection associated with the service. |
| `PrivateEndpointConnectionsSec_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Deletes a private endpoint connection. |
| `PrivateEndpointConnectionsSec_Get` | `EXEC` | `privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Gets the specified private endpoint connection associated with the service. |