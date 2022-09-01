---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - key_vault
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the key vault resource. |
| `name` | `string` | Name of the key vault resource. |
| `keySize` | `integer` | The key size in bits. For example: 2048, 3072, or 4096 for RSA. |
| `kty` | `string` | The type of the key. For valid values, see JsonWebKeyType. |
| `release_policy` | `object` |  |
| `curveName` | `string` | The elliptic curve name. For valid values, see JsonWebKeyCurveName. |
| `attributes` | `object` | The object attributes managed by the Azure Key Vault service. |
| `location` | `string` | Azure location of the key vault resource. |
| `keyUri` | `string` | The URI to retrieve the current version of the key. |
| `type` | `string` | Resource type of the key vault resource. |
| `keyOps` | `array` |  |
| `keyUriWithVersion` | `string` | The URI to retrieve the specific version of the key. |
| `tags` | `object` | Tags assigned to the key vault resource. |
| `rotationPolicy` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Keys_List` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Lists the keys in the specified key vault. |
| `Keys_CreateIfNotExist` | `EXEC` | `keyName, resourceGroupName, subscriptionId, vaultName, data__properties` | Creates the first version of a new key if it does not exist. If it already exists, then the existing key is returned without any write operations being performed. This API does not create subsequent versions, and does not update existing keys. |
| `Keys_Get` | `EXEC` | `keyName, resourceGroupName, subscriptionId, vaultName` | Gets the current version of the specified key from the specified key vault. |
| `Keys_GetVersion` | `EXEC` | `keyName, keyVersion, resourceGroupName, subscriptionId, vaultName` | Gets the specified version of the specified key in the specified key vault. |
| `Keys_ListVersions` | `EXEC` | `keyName, resourceGroupName, subscriptionId, vaultName` | Lists the versions of the specified key in the specified key vault. |
