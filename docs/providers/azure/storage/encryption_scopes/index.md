---
title: encryption_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_scopes
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
<tr><td><b>Name</b></td><td><code>encryption_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.encryption_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `keyVaultProperties` | `object` | The key vault properties for the encryption scope. This is a required field if encryption scope 'source' attribute is set to 'Microsoft.KeyVault'. |
| `state` | `string` | The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `lastModifiedTime` | `string` | Gets the last modification date and time of the encryption scope in UTC. |
| `source` | `string` | The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault. |
| `creationTime` | `string` | Gets the creation date and time of the encryption scope in UTC. |
| `requireInfrastructureEncryption` | `boolean` | A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EncryptionScopes_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all the encryption scopes available under the specified storage account. |
| `EncryptionScopes_Get` | `EXEC` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Returns the properties for the specified encryption scope. |
| `EncryptionScopes_Patch` | `EXEC` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Update encryption scope properties as specified in the request body. Update fails if the specified encryption scope does not already exist. |
| `EncryptionScopes_Put` | `EXEC` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Synchronously creates or updates an encryption scope under the specified storage account. If an encryption scope is already created and a subsequent request is issued with different properties, the encryption scope properties will be updated per the specified request. |
