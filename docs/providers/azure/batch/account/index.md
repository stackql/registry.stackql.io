---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - batch
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
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `poolAllocationMode` | `string` | The allocation mode for creating pools in the Batch account. |
| `allowedAuthenticationModes` | `array` | List of allowed authentication modes for the Batch account that can be used to authenticate with the data plane. This does not affect authentication with the control plane. |
| `dedicatedCoreQuota` | `integer` | For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned. |
| `lowPriorityCoreQuota` | `integer` | For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned. |
| `dedicatedCoreQuotaPerVMFamilyEnforced` | `boolean` | If this flag is true, dedicated core quota is enforced via both the dedicatedCoreQuotaPerVMFamily and dedicatedCoreQuota properties on the account. If this flag is false, dedicated core quota is enforced only via the dedicatedCoreQuota property on the account and does not consider Virtual Machine family. |
| `location` | `string` | The location of the resource. |
| `nodeManagementEndpoint` | `string` | The endpoint used by compute node to connect to the Batch node management service. |
| `dedicatedCoreQuotaPerVMFamily` | `array` | A list of the dedicated core quota per Virtual Machine family for the Batch account. For accounts with PoolAllocationMode set to UserSubscription, quota is managed on the subscription so this value is not returned. |
| `autoStorage` | `object` | Contains information about the auto-storage account associated with a Batch account. |
| `poolQuota` | `integer` |  |
| `publicNetworkAccess` | `string` | The network access type for operating on the resources in the Batch account. |
| `provisioningState` | `string` | The provisioned state of the resource |
| `accountEndpoint` | `string` | The account endpoint used to interact with the Batch service. |
| `keyVaultReference` | `object` | Identifies the Azure key vault associated with a Batch account. |
| `networkProfile` | `object` | Network profile for Batch account, which contains network rule settings for each endpoint. |
| `privateEndpointConnections` | `array` | List of private endpoint connections associated with the Batch account |
| `activeJobAndJobScheduleQuota` | `integer` |  |
| `tags` | `object` | The tags of the resource. |
| `encryption` | `object` | Configures how customer data is encrypted inside the Batch account. By default, accounts are encrypted using a Microsoft managed key. For additional control, a customer-managed key can be used instead. |
| `identity` | `object` | The identity of the Batch account, if configured. This is used when the user specifies 'Microsoft.KeyVault' as their Batch account encryption configuration or when `ManagedIdentity` is selected as the auto-storage authentication mode. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BatchAccount_List` | `SELECT` | `subscriptionId` | Gets information about the Batch accounts associated with the subscription. |
| `BatchAccount_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about the Batch accounts associated with the specified resource group. |
| `BatchAccount_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location` | Creates a new Batch account with the specified parameters. Existing accounts cannot be updated with this API and should instead be updated with the Update Batch Account API. |
| `BatchAccount_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes the specified Batch account. |
| `BatchAccount_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets information about the specified Batch account. |
| `BatchAccount_GetDetector` | `EXEC` | `accountName, detectorId, resourceGroupName, subscriptionId` | Gets information about the given detector for a given Batch account. |
| `BatchAccount_GetKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, getting the keys will fail. |
| `BatchAccount_ListDetectors` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets information about the detectors available for a given Batch account. |
| `BatchAccount_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the endpoints that a Batch Compute Node under this Batch Account may call as part of Batch service administration. If you are deploying a Pool inside of a virtual network that you specify, you must make sure your network allows outbound access to these endpoints. Failure to allow access to these endpoints may cause Batch to mark the affected nodes as unusable. For more information about creating a pool inside of a virtual network, see https://docs.microsoft.com/azure/batch/batch-virtual-network |
| `BatchAccount_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyName` | This operation applies only to Batch accounts with allowedAuthenticationModes containing 'SharedKey'. If the Batch account doesn't contain 'SharedKey' in its allowedAuthenticationMode, clients cannot use shared keys to authenticate, and must use another allowedAuthenticationModes instead. In this case, regenerating the keys will fail. |
| `BatchAccount_SynchronizeAutoStorageKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Synchronizes access keys for the auto-storage account configured for the specified Batch account, only if storage key authentication is being used. |
| `BatchAccount_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing Batch account. |
