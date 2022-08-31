---
title: server_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - server_keys
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
<tr><td><b>Name</b></td><td><code>server_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subregion` | `string` | Subregion of the server key. |
| `thumbprint` | `string` | Thumbprint of the server key. |
| `uri` | `string` | The URI of the server key. If the ServerKeyType is AzureKeyVault, then the URI is required. |
| `autoRotationEnabled` | `boolean` | Key auto rotation opt-in flag. Either true or false. |
| `creationDate` | `string` | The server key creation date. |
| `kind` | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `serverKeyType` | `string` | The server key type like 'ServiceManaged', 'AzureKeyVault'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerKeys_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server keys. |
| `ServerKeys_CreateOrUpdate` | `INSERT` | `keyName, resourceGroupName, serverName, subscriptionId` | Creates or updates a server key. |
| `ServerKeys_Delete` | `DELETE` | `keyName, resourceGroupName, serverName, subscriptionId` | Deletes the server key with the given name. |
| `ServerKeys_Get` | `EXEC` | `keyName, resourceGroupName, serverName, subscriptionId` | Gets a server key. |
