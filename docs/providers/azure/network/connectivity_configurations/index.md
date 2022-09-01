---
title: connectivity_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - connectivity_configurations
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
<tr><td><b>Name</b></td><td><code>connectivity_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.connectivity_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `description` | `string` | A description of the connectivity configuration. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `hubs` | `array` | List of hubItems |
| `type` | `string` | Resource type. |
| `appliesToGroups` | `array` | Groups for configuration |
| `connectivityTopology` | `string` | Connectivity topology type. |
| `provisioningState` | `string` | The current provisioning state. |
| `isGlobal` | `string` | Flag if global mesh is supported. |
| `deleteExistingPeering` | `string` | Flag if need to remove current existing peerings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConnectivityConfigurations_List` | `SELECT` | `networkManagerName, resourceGroupName, subscriptionId` | Lists all the network manager connectivity configuration in a specified network manager. |
| `ConnectivityConfigurations_CreateOrUpdate` | `INSERT` |  | Creates/Updates a new network manager connectivity configuration |
| `ConnectivityConfigurations_Delete` | `DELETE` |  | Deletes a network manager connectivity configuration, specified by the resource group, network manager name, and connectivity configuration name |
| `ConnectivityConfigurations_Get` | `EXEC` |  | Gets a Network Connectivity Configuration, specified by the resource group, network manager name, and connectivity Configuration name |
