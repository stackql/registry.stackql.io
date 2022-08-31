---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - sql
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
<tr><td><b>Id</b></td><td><code>azure.sql.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `primaryUserAssignedIdentityId` | `string` | The resource id of a user assigned identity to be used by default. |
| `version` | `string` | The version of the server. |
| `administrators` | `object` | Properties of a active directory administrator. |
| `restrictOutboundNetworkAccess` | `string` | Whether or not to restrict outbound network access for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled' |
| `location` | `string` | Resource location. |
| `workspaceFeature` | `string` | Whether or not existing server has a workspace created and if it allows connection from workspace |
| `privateEndpointConnections` | `array` | List of private endpoint connections on a server |
| `publicNetworkAccess` | `string` | Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled' |
| `federatedClientId` | `string` | The Client id used for cross tenant CMK scenario |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of the server. |
| `state` | `string` | The state of the server. |
| `keyId` | `string` | A CMK URI of the key to use for encryption. |
| `administratorLogin` | `string` | Administrator username for the server. Once created it cannot be changed. |
| `administratorLoginPassword` | `string` | The administrator login password (required for server creation). |
| `kind` | `string` | Kind of sql server. This is metadata used for the Azure portal experience. |
| `minimalTlsVersion` | `string` | Minimal TLS version. Allowed values: '1.0', '1.1', '1.2' |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Servers_List` | `SELECT` | `subscriptionId` | Gets a list of all servers in the subscription. |
| `Servers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of servers in a resource groups. |
| `Servers_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates a server. |
| `Servers_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes a server. |
| `Servers_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Determines whether a resource can be created with the specified name. |
| `Servers_Get` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a server. |
| `Servers_ImportDatabase` | `EXEC` | `resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri` | Imports a bacpac into a new database. |
| `Servers_Update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates a server. |
