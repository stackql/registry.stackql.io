---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - databricks
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
<tr><td><b>Id</b></td><td><code>azure.databricks.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `uiDefinitionUri` | `string` | The blob URI where the UI definition file is located. |
| `updatedBy` | `object` | Provides details of the entity that created/updated the workspace. |
| `parameters` | `object` | Custom Parameters used for Cluster Creation. |
| `authorizations` | `array` | The workspace provider authorizations. |
| `privateEndpointConnections` | `array` | Private endpoint connections created on the workspace |
| `encryption` | `object` | Encryption properties for databricks workspace |
| `storageAccountIdentity` | `object` | The Managed Identity details for storage account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `managedResourceGroupId` | `string` | The managed resource group Id. |
| `sku` | `object` | SKU for the resource. |
| `requiredNsgRules` | `string` | Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only. |
| `location` | `string` | The geo-location where the resource lives |
| `workspaceUrl` | `string` | The workspace URL which is of the format 'adb-{workspaceId}.{random}.azuredatabricks.net' |
| `workspaceId` | `string` | The unique identifier of the databricks workspace in databricks control plane. |
| `publicNetworkAccess` | `string` | The network access type for accessing workspace. Set value to disabled to access workspace only via private link. |
| `createdDateTime` | `string` | The date and time stamp when the workspace was created. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | Provisioning status of the workspace. |
| `createdBy` | `object` | Provides details of the entity that created/updated the workspace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the workspaces within a resource group. |
| `Workspaces_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the workspaces within a subscription. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates a new workspace. |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes the workspace. |
| `Workspaces_Get` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets the workspace. |
| `Workspaces_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a workspace. |