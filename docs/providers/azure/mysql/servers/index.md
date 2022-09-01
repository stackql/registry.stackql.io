---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - mysql
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `privateEndpointConnections` | `array` | List of private endpoint connections on a server |
| `publicNetworkAccess` | `string` | Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of a server. |
| `version` | `string` | The version of a server. |
| `administratorLogin` | `string` | The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation). |
| `replicationRole` | `string` | The replication role of the server. |
| `tags` | `object` | Resource tags. |
| `earliestRestoreDate` | `string` | Earliest restore point creation time (ISO8601 format) |
| `masterServerId` | `string` | The master server id of a replica server. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `minimalTlsVersion` | `string` | Enforce a minimal Tls version for the server. |
| `replicaCapacity` | `integer` | The maximum number of replicas that a master server can have. |
| `sku` | `object` | The resource model definition representing SKU |
| `infrastructureEncryption` | `string` | Add a second layer of encryption for your data using new encryption algorithm which gives additional data protection. Value is optional but if passed in, must be 'Disabled' or 'Enabled'. |
| `storageProfile` | `object` | Storage Profile properties of a server |
| `location` | `string` | The geo-location where the resource lives |
| `byokEnforcement` | `string` | Status showing whether the server data encryption is enabled with customer-managed keys. |
| `userVisibleState` | `string` | A state of a server that is visible to user. |
| `sslEnforcement` | `string` | Enable ssl enforcement or not when connect to server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_List` | `SELECT` | `subscriptionId` | List all the servers in a given subscription. |
| `Servers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `Servers_Create` | `INSERT` | `resourceGroupName, serverName, subscriptionId, data__location, data__properties` | Creates a new server or updates an existing server. The update action will overwrite the existing server. |
| `Servers_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `Servers_Get` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets information about a server. |
| `Servers_Restart` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Restarts a server. |
| `Servers_Start` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Starts a stopped server. |
| `Servers_Stop` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Stops a running server. |
| `Servers_Update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
| `Servers_Upgrade` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Upgrade server version. |
