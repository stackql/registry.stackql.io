---
title: server_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - server_endpoints
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>server_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.server_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `volumeFreeSpacePercent` | `integer` | Level of free space to be maintained by Cloud Tiering if it is enabled. |
| `offlineDataTransferShareName` | `string` | Offline data transfer share name |
| `lastOperationName` | `string` | Resource Last Operation Name |
| `lastWorkflowId` | `string` | ServerEndpoint lastWorkflowId |
| `serverResourceId` | `string` | Arm resource identifier. |
| `offlineDataTransferStorageAccountResourceId` | `string` | Offline data transfer storage account resource ID |
| `syncStatus` | `object` | Server Endpoint sync status |
| `offlineDataTransferStorageAccountTenantId` | `string` | Offline data transfer storage account tenant ID |
| `localCacheMode` | `string` | Policy for enabling follow-the-sun business models: link local cache to cloud behavior to pre-populate before local access. |
| `initialDownloadPolicy` | `string` | Policy for how namespace and files are recalled during FastDr |
| `serverName` | `string` | Server name |
| `cloudTieringStatus` | `object` | Server endpoint cloud tiering status object. |
| `friendlyName` | `string` | Friendly Name |
| `provisioningState` | `string` | ServerEndpoint Provisioning State |
| `serverLocalPath` | `string` | Server folder used for data synchronization |
| `cloudTiering` | `string` | Type of the Feature Status |
| `tierFilesOlderThanDays` | `integer` | Tier files older than days. |
| `initialUploadPolicy` | `string` | Policy for how the initial upload sync session is performed. |
| `recallStatus` | `object` | Server endpoint recall status object. |
| `offlineDataTransfer` | `string` | Type of the Feature Status |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerEndpoints_ListBySyncGroup` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint list. |
| `ServerEndpoints_Create` | `INSERT` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new ServerEndpoint. |
| `ServerEndpoints_Delete` | `DELETE` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given ServerEndpoint. |
| `ServerEndpoints_Get` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a ServerEndpoint. |
| `ServerEndpoints_Update` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Patch a given ServerEndpoint. |
| `ServerEndpoints_recallAction` | `EXEC` | `resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName` | Recall a server endpoint. |
