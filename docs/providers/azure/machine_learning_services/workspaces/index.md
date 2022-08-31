---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - machine_learning_services
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
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | The description of this workspace. |
| `privateLinkCount` | `integer` | Count of private connections in the workspace |
| `scheduledPurgeDate` | `string` | The timestamp when the soft deleted workspace is going to be purged |
| `publicNetworkAccess` | `string` | Whether requests from Public Network are allowed. |
| `serviceManagedResourcesSettings` | `object` |  |
| `storageHnsEnabled` | `boolean` | If the storage associated with the workspace has hierarchical namespace(HNS) enabled. |
| `softDeletedAt` | `string` | The timestamp when the workspace was soft deleted |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `tenantId` | `string` | The tenant id associated with this workspace. |
| `primaryUserAssignedIdentity` | `string` | The user assigned identity resource id that represents the workspace identity. |
| `workspaceId` | `string` | The immutable id associated with this workspace. |
| `discoveryUrl` | `string` | Url for the discovery service to identify regional endpoints for machine learning experimentation services |
| `keyVault` | `string` | ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created |
| `storageAccount` | `string` | ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created |
| `encryption` | `object` |  |
| `allowPublicAccessWhenBehindVnet` | `boolean` | The flag to indicate whether to allow public access when behind VNet. |
| `sharedPrivateLinkResources` | `array` | The list of shared private link resources in this workspace. |
| `imageBuildCompute` | `string` | The compute name for image build |
| `notebookInfo` | `object` |  |
| `containerRegistry` | `string` | ARM id of the container registry associated with this workspace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `friendlyName` | `string` | The friendly name for this workspace. This name in mutable |
| `provisioningState` | `string` | The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning. |
| `sku` | `object` | The resource model definition representing SKU |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `serviceProvisionedResourceGroup` | `string` | The name of the managed resource group created by workspace RP in customer subscription if the workspace is CMK workspace |
| `v1LegacyMode` | `boolean` | Enabling v1_legacy_mode may prevent you from using features provided by the v2 API. |
| `location` | `string` | Specifies the location of the resource. |
| `mlFlowTrackingUri` | `string` | The URI associated with this workspace that machine learning flow must point at to set up tracking. |
| `hbiWorkspace` | `boolean` | The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service |
| `privateEndpointConnections` | `array` | The list of private endpoint connections in the workspace. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `applicationInsights` | `string` | ARM id of the application insights associated with this workspace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available machine learning workspaces under the specified resource group. |
| `Workspaces_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the available machine learning workspaces under the specified subscription. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace with the specified parameters. |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a machine learning workspace. |
| `Workspaces_Diagnose` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |  |
| `Workspaces_Get` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified machine learning workspace. |
| `Workspaces_ListKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry |
| `Workspaces_ListNotebookAccessToken` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | return notebook access token and refresh token |
| `Workspaces_ListNotebookKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List keys of a notebook. |
| `Workspaces_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |  |
| `Workspaces_ListStorageAccountKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List storage account keys of a workspace. |
| `Workspaces_PrepareNotebook` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Prepare a notebook. |
| `Workspaces_ResyncKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry |
| `Workspaces_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a machine learning workspace with the specified parameters. |
