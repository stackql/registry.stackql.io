---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - postgresql
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
<tr><td><b>Id</b></td><td><code>azure.postgresql.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `network` | `object` | Network properties of a server |
| `tags` | `object` | Resource tags. |
| `administratorLogin` | `string` | The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation). |
| `sku` | `object` | The resource model definition representing SKU |
| `availabilityZone` | `string` | availability zone information of the server. |
| `version` | `string` | The version of a server. |
| `createMode` | `string` | The mode to create a new PostgreSQL server. |
| `storage` | `object` | Storage properties of a server |
| `administratorLoginPassword` | `string` | The administrator login password (required for server creation). |
| `pointInTimeUTC` | `string` | Restore point creation time (ISO8601 format), specifying the time to restore from. It's required when 'createMode' is 'PointInTimeRestore'. |
| `sourceServerResourceId` | `string` | The source server resource ID to restore from. It's required when 'createMode' is 'PointInTimeRestore'. |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of a server. |
| `backup` | `object` | Backup properties of a server |
| `state` | `string` | A state of a server that is visible to user. |
| `highAvailability` | `object` | High availability properties of a server |
| `maintenanceWindow` | `object` | Maintenance window properties of a server. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `minorVersion` | `string` | The minor version of the server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_List` | `SELECT` | `subscriptionId` | List all the servers in a given subscription. |
| `Servers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the servers in a given resource group. |
| `Servers_Create` | `INSERT` | `resourceGroupName, serverName, subscriptionId` | Creates a new server. |
| `Servers_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `Servers_Get` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets information about a server. |
| `Servers_Restart` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Restarts a server. |
| `Servers_Start` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Starts a server. |
| `Servers_Stop` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Stops a server. |
| `Servers_Update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates an existing server. The request body can contain one to many of the properties present in the normal server definition. |
