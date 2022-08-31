---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - hdinsight
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
<tr><td><b>Id</b></td><td><code>azure.hdinsight.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `privateEndpoint` | `object` | The private endpoint. |
| `privateLinkServiceConnectionState` | `object` | The private link service connection state. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `linkIdentifier` | `string` | The link identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists the private endpoint connections for a HDInsight cluster. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection manually. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes the specific private endpoint connection. |
| `PrivateEndpointConnections_Get` | `EXEC` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specific private endpoint connection. |
