---
title: mhsm_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_private_endpoint_connections
  - key_vault
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
<tr><td><b>Name</b></td><td><code>mhsm_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.mhsm_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| `name` | `string` | The name of the managed HSM Pool. |
| `location` | `string` | The supported Azure location where the managed HSM Pool should be created. |
| `privateEndpoint` | `object` | Private endpoint object properties. |
| `etag` | `string` | Modified whenever there is a change in the state of private endpoint connection. |
| `tags` | `object` | Resource tags |
| `type` | `string` | The resource type of the managed HSM Pool. |
| `provisioningState` | `string` | The current provisioning state. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| `privateLinkServiceConnectionState` | `object` | An object that represents the approval state of the private link connection. |
| `sku` | `object` | SKU details |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MHSMPrivateEndpointConnections_ListByResource` | `SELECT` | `name, resourceGroupName, subscriptionId` | The List operation gets information about the private endpoint connections associated with the managed HSM Pool. |
| `MHSMPrivateEndpointConnections_Delete` | `DELETE` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint connection associated with the managed hsm pool. |
| `MHSMPrivateEndpointConnections_Get` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specified private endpoint connection associated with the managed HSM Pool. |
| `MHSMPrivateEndpointConnections_Put` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Updates the specified private endpoint connection associated with the managed hsm pool. |