---
title: appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances
  - resource_connector
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
<tr><td><b>Name</b></td><td><code>appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_connector.appliances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | Appliance’s health and state of connection to on-prem |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `identity` | `object` | Identity for the resource. |
| `provisioningState` | `string` | The current deployment or provisioning state, which only appears in the response. |
| `version` | `string` | Version of the Appliance |
| `infrastructureConfig` | `object` | Contains infrastructure information about the Appliance |
| `tags` | `object` | Resource tags. |
| `distro` | `string` | Represents a supported Fabric/Infra. (AKSEdge etc...). |
| `publicKey` | `string` | Certificates pair used to download MSI certificate from HIS |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Appliances_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Appliances in the specified subscription and resource group. The operation returns properties of each Appliance. |
| `Appliances_ListBySubscription` | `SELECT` | `subscriptionId` | Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance |
| `Appliances_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates or updates an Appliance in the specified Subscription and Resource Group. |
| `Appliances_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes an Appliance with the specified Resource Name, Resource Group, and Subscription Id. |
| `Appliances_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets the details of an Appliance with a specified resource group and name. |
| `Appliances_GetUpgradeGraph` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, upgradeGraph` | Gets the upgrade graph of an Appliance with a specified resource group and name and specific release train. |
| `Appliances_ListClusterCustomerUserCredential` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns the cluster customer user credentials for the dedicated appliance. |
| `Appliances_ListClusterUserCredential` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns the cluster user credentials for the dedicated appliance. |
| `Appliances_ListOperations` | `EXEC` |  | Lists all available Appliances operations. |
| `Appliances_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates an Appliance with the specified Resource Name in the specified Resource Group and Subscription. |
