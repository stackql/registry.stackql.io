---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - redis_enterprise
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis_enterprise.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceState` | `string` | Current resource status |
| `clusteringPolicy` | `string` | Clustering policy - default is OSSCluster. Specified at create time. |
| `persistence` | `object` | Persistence-related configuration for the RedisEnterprise database |
| `clientProtocol` | `string` | Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted. |
| `provisioningState` | `string` | Current provisioning status |
| `modules` | `array` | Optional set of redis modules to enable in this database - modules can only be added at creation time. |
| `geoReplication` | `object` | Optional set of properties to configure geo replication for this database. |
| `port` | `integer` | TCP port of the database endpoint. Specified at create time. Defaults to an available port. |
| `evictionPolicy` | `string` | Redis eviction policy - default is VolatileLRU |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Databases_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets all databases in the specified RedisEnterprise cluster. |
| `Databases_Create` | `INSERT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Creates a database |
| `Databases_Delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Deletes a single database |
| `Databases_Export` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUri` | Exports a database file from target database. |
| `Databases_ForceUnlink` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__ids` | Forcibly removes the link to the specified database resource. |
| `Databases_Get` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Gets information about a database in a RedisEnterprise cluster. |
| `Databases_Import` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUris` | Imports database files to target database. |
| `Databases_ListKeys` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Retrieves the access keys for the RedisEnterprise database. |
| `Databases_RegenerateKey` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the RedisEnterprise database's access keys. |
| `Databases_Update` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Updates a database |
