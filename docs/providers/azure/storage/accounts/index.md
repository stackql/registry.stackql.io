---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - storage
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `primaryEndpoints` | `object` | The URIs that are used to perform a retrieval of a public blob, queue, table, web or dfs object. |
| `isLocalUserEnabled` | `boolean` | Enables local users feature, if set to true |
| `secondaryLocation` | `string` | Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS. |
| `statusOfPrimary` | `string` | Gets the status indicating whether the primary location of the storage account is available or unavailable. |
| `dnsEndpointType` | `string` | Allows you to specify the type of endpoint. Set this to AzureDNSZone to create a large number of accounts in a single subscription, which creates accounts in an Azure DNS Zone and the endpoint URL will have an alphanumeric DNS Zone identifier. |
| `sku` | `object` | The resource model definition representing SKU |
| `isHnsEnabled` | `boolean` | Account HierarchicalNamespace enabled if sets to true. |
| `location` | `string` | The geo-location where the resource lives |
| `storageAccountSkuConversionStatus` | `object` | This defines the sku conversion status object for asynchronous sku conversions. |
| `privateEndpointConnections` | `array` | List of private endpoint connection associated with the specified storage account |
| `supportsHttpsTrafficOnly` | `boolean` | Allows https traffic only to storage service if sets to true. |
| `tags` | `object` | Resource tags. |
| `accessTier` | `string` | Required for storage accounts where kind = BlobStorage. The access tier is used for billing. The 'Premium' access tier is the default value for premium block blobs storage account type and it cannot be changed for the premium block blobs storage account type. |
| `immutableStorageWithVersioning` | `object` | This property enables and defines account-level immutability. Enabling the feature auto-enables Blob Versioning. |
| `keyCreationTime` | `object` | Storage account keys creation time. |
| `allowedCopyScope` | `string` | Restrict copy to and from Storage Accounts within an AAD tenant or with Private Links to the same VNet. |
| `secondaryEndpoints` | `object` | The URIs that are used to perform a retrieval of a public blob, queue, table, web or dfs object. |
| `primaryLocation` | `string` | Gets the location of the primary data center for the storage account. |
| `allowSharedKeyAccess` | `boolean` | Indicates whether the storage account permits requests to be authorized with the account access key via Shared Key. If false, then all requests, including shared access signatures, must be authorized with Azure Active Directory (Azure AD). The default value is null, which is equivalent to true. |
| `keyPolicy` | `object` | KeyPolicy assigned to the storage account. |
| `minimumTlsVersion` | `string` | Set the minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property. |
| `blobRestoreStatus` | `object` | Blob restore status. |
| `creationTime` | `string` | Gets the creation date and time of the storage account in UTC. |
| `isSftpEnabled` | `boolean` | Enables Secure File Transfer Protocol, if set to true |
| `networkAcls` | `object` | Network rule set |
| `isNfsV3Enabled` | `boolean` | NFS 3.0 protocol support enabled if set to true. |
| `allowCrossTenantReplication` | `boolean` | Allow or disallow cross AAD tenant object replication. The default interpretation is true for this property. |
| `statusOfSecondary` | `string` | Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. |
| `publicNetworkAccess` | `string` | Allow or disallow public network access to Storage Account. Value is optional but if passed in, must be 'Enabled' or 'Disabled'. |
| `identity` | `object` | Identity for the resource. |
| `failoverInProgress` | `boolean` | If the failover is in progress, the value will be true, otherwise, it will be null. |
| `defaultToOAuthAuthentication` | `boolean` | A boolean flag which indicates whether the default authentication is OAuth or not. The default interpretation is false for this property. |
| `geoReplicationStats` | `object` | Statistics related to replication for storage account's Blob, Table, Queue and File services. It is only available when geo-redundant replication is enabled for the storage account. |
| `sasPolicy` | `object` | SasPolicy assigned to the storage account. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `encryption` | `object` | The encryption settings on the storage account. |
| `azureFilesIdentityBasedAuthentication` | `object` | Settings for Azure Files identity based authentication. |
| `routingPreference` | `object` | Routing preference defines the type of network, either microsoft or internet routing to be used to deliver the user data, the default option is microsoft routing |
| `provisioningState` | `string` | Gets the status of the storage account at the time the operation was called. |
| `lastGeoFailoverTime` | `string` | Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS. |
| `customDomain` | `object` | The custom domain assigned to this storage account. This can be set via Update. |
| `largeFileSharesState` | `string` | Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled. |
| `kind` | `string` | Gets the Kind. |
| `allowBlobPublicAccess` | `boolean` | Allow or disallow public access to all blobs or containers in the storage account. The default interpretation is true for this property. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageAccounts_List` | `SELECT` | `subscriptionId` | Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this. |
| `StorageAccounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this. |
| `StorageAccounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku` | Asynchronously creates a new storage account with the specified parameters. If an account is already created and a subsequent create request is issued with different properties, the account properties will be updated. If an account is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed. |
| `StorageAccounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes a storage account in Microsoft Azure. |
| `StorageAccounts_AbortHierarchicalNamespaceMigration` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Abort live Migration of storage account to enable Hns |
| `StorageAccounts_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the storage account name is valid and is not already in use. |
| `StorageAccounts_Failover` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Failover request can be triggered for a storage account in case of availability issues. The failover occurs from the storage account's primary cluster to secondary cluster for RA-GRS accounts. The secondary cluster will become primary after failover. |
| `StorageAccounts_GetProperties` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys. |
| `StorageAccounts_HierarchicalNamespaceMigration` | `EXEC` | `accountName, requestType, resourceGroupName, subscriptionId` | Live Migration of storage account to enable Hns |
| `StorageAccounts_ListAccountSAS` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__signedExpiry, data__signedPermission, data__signedResourceTypes, data__signedServices` | List SAS credentials of a storage account. |
| `StorageAccounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the access keys or Kerberos keys (if active directory enabled) for the specified storage account. |
| `StorageAccounts_ListServiceSAS` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__canonicalizedResource` | List service SAS credentials of a specific resource. |
| `StorageAccounts_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyName` | Regenerates one of the access keys or Kerberos keys for the specified storage account. |
| `StorageAccounts_RestoreBlobRanges` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__blobRanges, data__timeToRestore` | Restore blobs in the specified blob ranges |
| `StorageAccounts_RevokeUserDelegationKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Revoke user delegation keys. |
| `StorageAccounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | The update operation can be used to update the SKU, encryption, access tier, or tags for a storage account. It can also be used to map the account to a custom domain. Only one custom domain is supported per storage account; the replacement/change of custom domain is not supported. In order to replace an old custom domain, the old value must be cleared/unregistered before a new value can be set. The update of multiple properties is supported. This call does not change the storage keys for the account. If you want to change the storage account keys, use the regenerate keys operation. The location and name of the storage account cannot be changed after creation. |
