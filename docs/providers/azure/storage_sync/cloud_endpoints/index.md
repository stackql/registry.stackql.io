---
title: cloud_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_endpoints
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
<tr><td><b>Name</b></td><td><code>cloud_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.cloud_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `partnershipId` | `string` | Partnership Id |
| `storageAccountResourceId` | `string` | Storage Account Resource Id |
| `changeEnumerationStatus` | `object` | Cloud endpoint change enumeration status object |
| `backupEnabled` | `string` | Backup Enabled |
| `provisioningState` | `string` | CloudEndpoint Provisioning State |
| `storageAccountTenantId` | `string` | Storage Account Tenant Id |
| `lastOperationName` | `string` | Resource Last Operation Name |
| `azureFileShareName` | `string` | Azure file share name |
| `friendlyName` | `string` | Friendly Name |
| `lastWorkflowId` | `string` | CloudEndpoint lastWorkflowId |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudEndpoints_ListBySyncGroup` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a CloudEndpoint List. |
| `CloudEndpoints_Create` | `INSERT` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new CloudEndpoint. |
| `CloudEndpoints_Delete` | `DELETE` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given CloudEndpoint. |
| `CloudEndpoints_Get` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a given CloudEndpoint. |
| `CloudEndpoints_PostBackup` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Post Backup a given CloudEndpoint. |
| `CloudEndpoints_PostRestore` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Post Restore a given CloudEndpoint. |
| `CloudEndpoints_PreBackup` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Pre Backup a given CloudEndpoint. |
| `CloudEndpoints_PreRestore` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Pre Restore a given CloudEndpoint. |
| `CloudEndpoints_TriggerChangeDetection` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint. |
| `CloudEndpoints_restoreheartbeat` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Restore Heartbeat a given CloudEndpoint. |
