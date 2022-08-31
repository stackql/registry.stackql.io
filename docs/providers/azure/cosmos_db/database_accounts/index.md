---
title: database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.database_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `apiProperties` | `object` |  |
| `ipRules` | `array` | Array of IpAddressOrRange objects. |
| `enableFreeTier` | `boolean` | Flag to indicate whether Free Tier is enabled. |
| `capabilities` | `array` | List of Cosmos DB capabilities for the account |
| `keysMetadata` | `object` | The metadata related to each access key for the given Cosmos DB database account. |
| `virtualNetworkRules` | `array` | List of Virtual Network ACL rules configured for the Cosmos DB account. |
| `instanceId` | `string` | A unique identifier assigned to the database account |
| `privateEndpointConnections` | `array` | List of Private Endpoint Connections configured for the Cosmos DB account. |
| `publicNetworkAccess` | `string` | Whether requests from Public Network are allowed |
| `networkAclBypassResourceIds` | `array` | An array that contains the Resource Ids for Network Acl Bypass for the Cosmos DB account. |
| `enableAnalyticalStorage` | `boolean` | Flag to indicate whether to enable storage analytics. |
| `enableCassandraConnector` | `boolean` | Enables the cassandra connector on the Cosmos DB C* account |
| `connectorOffer` | `string` | The cassandra connector offer type for the Cosmos DB C* database account. |
| `defaultIdentity` | `string` | The default identity for accessing key vault used in features like customer managed keys. The default identity needs to be explicitly set by the users. It can be "FirstPartyIdentity", "SystemAssignedIdentity" and more. |
| `backupPolicy` | `object` | The object representing the policy for taking backups on an account. |
| `keyVaultKeyUri` | `string` | The URI of the key vault |
| `analyticalStorageConfiguration` | `object` | Analytical storage specific properties. |
| `networkAclBypass` | `string` | Indicates what services are allowed to bypass firewall checks. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | Indicates the type of database account. This can only be set at database account creation. |
| `capacity` | `object` | The object that represents all properties related to capacity enforcement on an account. |
| `isVirtualNetworkFilterEnabled` | `boolean` | Flag to indicate whether to enable/disable Virtual Network ACL rules. |
| `location` | `string` | The location of the resource group to which the resource belongs. |
| `tags` | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| `documentEndpoint` | `string` | The connection endpoint for the Cosmos DB database account. |
| `enableAutomaticFailover` | `boolean` | Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account. |
| `failoverPolicies` | `array` | An array that contains the regions ordered by their failover priorities. |
| `provisioningState` | `string` | The status of the Cosmos DB account at the time the operation was called. The status can be one of following. 'Creating' – the Cosmos DB account is being created. When an account is in Creating state, only properties that are specified as input for the Create Cosmos DB account operation are returned. 'Succeeded' – the Cosmos DB account is active for use. 'Updating' – the Cosmos DB account is being updated. 'Deleting' – the Cosmos DB account is being deleted. 'Failed' – the Cosmos DB account failed creation. 'DeletionFailed' – the Cosmos DB account deletion failed. |
| `writeLocations` | `array` | An array that contains the write location for the Cosmos DB account. |
| `enableMaterializedViews` | `boolean` | Flag to indicate whether to enable MaterializedViews on the Cosmos DB account |
| `cors` | `array` | The CORS policy for the Cosmos DB database account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `createMode` | `string` | Enum to indicate the mode of account creation. |
| `readLocations` | `array` | An array that contains of the read locations enabled for the Cosmos DB account. |
| `diagnosticLogSettings` | `object` | Indicates what diagnostic log settings are to be enabled. |
| `type` | `string` | The type of Azure resource. |
| `consistencyPolicy` | `object` | The consistency policy for the Cosmos DB database account. |
| `databaseAccountOfferType` | `string` | The offer type for the Cosmos DB database account. |
| `restoreParameters` | `object` | Parameters to indicate the information about the restore. |
| `disableLocalAuth` | `boolean` | Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication. |
| `locations` | `array` | An array that contains all of the locations enabled for the Cosmos DB account. |
| `disableKeyBasedMetadataWriteAccess` | `boolean` | Disable write operations on metadata resources (databases, containers, throughput) via account keys |
| `enableMultipleWriteLocations` | `boolean` | Enables the account to write in multiple locations |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseAccounts_List` | `SELECT` | `subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| `DatabaseAccounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| `DatabaseAccounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account. |
| `DatabaseAccounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB database account. |
| `DatabaseAccounts_CheckNameExists` | `EXEC` | `accountName` | Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 50 characters. |
| `DatabaseAccounts_FailoverPriorityChange` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__failoverPolicies` | Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. |
| `DatabaseAccounts_Get` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB database account. |
| `DatabaseAccounts_GetReadOnlyKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the read-only access keys for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListConnectionStrings` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the connection strings for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the access keys for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListMetricDefinitions` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves metric definitions for the given database account. |
| `DatabaseAccounts_ListMetrics` | `EXEC` | `$filter, accountName, resourceGroupName, subscriptionId` | Retrieves the metrics determined by the given filter for the given database account. |
| `DatabaseAccounts_ListReadOnlyKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the read-only access keys for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListUsages` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the usages (most recent data) for the given database account. |
| `DatabaseAccounts_OfflineRegion` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__region` | Offline the specified region for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_OnlineRegion` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__region` | Online the specified region for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyKind` | Regenerates an access key for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing Azure Cosmos DB database account. |
