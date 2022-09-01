---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - maria_db
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
<tr><td><b>Id</b></td><td><code>azure.maria_db.replicas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `storageProfile` | `object` | Storage Profile properties of a server |
| `replicationRole` | `string` | The replication role of the server. |
| `version` | `string` | The version of a server. |
| `administratorLogin` | `string` | The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation). |
| `publicNetworkAccess` | `string` | Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' |
| `minimalTlsVersion` | `string` | Enforce a minimal Tls version for the server. |
| `replicaCapacity` | `integer` | The maximum number of replicas that a master server can have. |
| `userVisibleState` | `string` | A state of a server that is visible to user. |
| `earliestRestoreDate` | `string` | Earliest restore point creation time (ISO8601 format) |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of a server. |
| `privateEndpointConnections` | `array` | List of private endpoint connections on a server |
| `sku` | `object` | Billing information related properties of a server. |
| `location` | `string` | The geo-location where the resource lives |
| `masterServerId` | `string` | The master server id of a replica server. |
| `sslEnforcement` | `string` | Enable ssl enforcement or not when connect to server. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Replicas_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
