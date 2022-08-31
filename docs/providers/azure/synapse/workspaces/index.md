---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - synapse
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedVirtualNetwork` | `string` | Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user. |
| `workspaceUID` | `string` | The workspace unique identifier |
| `managedResourceGroupName` | `string` | Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.' |
| `location` | `string` | The geo-location where the resource lives |
| `cspWorkspaceAdminProperties` | `object` | Initial workspace AAD admin properties for a CSP subscription |
| `provisioningState` | `string` | Resource provisioning state |
| `settings` | `object` | Workspace settings |
| `extraProperties` | `object` | Workspace level configs and feature flags |
| `publicNetworkAccess` | `string` | Enable or Disable public network access to workspace |
| `tags` | `object` | Resource tags. |
| `managedVirtualNetworkSettings` | `object` | Managed Virtual Network Settings |
| `workspaceRepositoryConfiguration` | `object` | Git integration settings |
| `virtualNetworkProfile` | `object` | Virtual Network Profile |
| `trustedServiceBypassEnabled` | `boolean` | Is trustedServiceBypassEnabled for the workspace |
| `sqlAdministratorLogin` | `string` | Login for workspace SQL active directory administrator |
| `privateEndpointConnections` | `array` | Private endpoint connections to the workspace |
| `azureADOnlyAuthentication` | `boolean` | Enable or Disable AzureADOnlyAuthentication on All Workspace subresource |
| `defaultDataLakeStorage` | `object` | Details of the data lake storage account associated with the workspace |
| `purviewConfiguration` | `object` | Purview Configuration |
| `sqlAdministratorLoginPassword` | `string` | SQL administrator login password |
| `encryption` | `object` | Details of the encryption associated with the workspace |
| `connectivityEndpoints` | `object` | Connectivity endpoints |
| `identity` | `object` | The workspace managed identity |
| `adlaResourceId` | `string` | The ADLA resource ID. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_List` | `SELECT` | `subscriptionId` | Returns a list of workspaces in a subscription |
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns a list of workspaces in a resource group |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a workspace |
| `Workspaces_Get` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets a workspace |
| `Workspaces_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a workspace |
