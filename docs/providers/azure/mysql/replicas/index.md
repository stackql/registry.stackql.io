---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
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
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.replicas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `userVisibleState` | `string` | A state of a server that is visible to user. |
| `version` | `string` | The version of a server. |
| `minimalTlsVersion` | `string` | Enforce a minimal Tls version for the server. |
| `replicationRole` | `string` | The replication role of the server. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `masterServerId` | `string` | The master server id of a replica server. |
| `publicNetworkAccess` | `string` | Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' |
| `infrastructureEncryption` | `string` | Add a second layer of encryption for your data using new encryption algorithm which gives additional data protection. Value is optional but if passed in, must be 'Disabled' or 'Enabled'. |
| `administratorLogin` | `string` | The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation). |
| `location` | `string` | The geo-location where the resource lives |
| `sslEnforcement` | `string` | Enable ssl enforcement or not when connect to server. |
| `privateEndpointConnections` | `array` | List of private endpoint connections on a server |
| `storageProfile` | `object` | Storage Profile properties of a server |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of a server. |
| `tags` | `object` | Resource tags. |
| `replicaCapacity` | `integer` | The maximum number of replicas that a master server can have. |
| `byokEnforcement` | `string` | Status showing whether the server data encryption is enabled with customer-managed keys. |
| `earliestRestoreDate` | `string` | Earliest restore point creation time (ISO8601 format) |
| `sku` | `object` | The resource model definition representing SKU |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Replicas_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
