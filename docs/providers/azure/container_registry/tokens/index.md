---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - container_registry
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `provisioningState` | `string` | Provisioning state of the resource. |
| `scopeMapId` | `string` | The resource ID of the scope map to which the token will be associated with. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `creationDate` | `string` | The creation date of scope map. |
| `credentials` | `object` | The properties of the credentials that can be used for authenticating the token. |
| `status` | `string` | The status of the token example enabled or disabled. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tokens_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the tokens for the specified container registry. |
| `Tokens_Create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, tokenName` | Creates a token for a container registry with the specified parameters. |
| `Tokens_Delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId, tokenName` | Deletes a token from a container registry. |
| `Tokens_Get` | `EXEC` | `registryName, resourceGroupName, subscriptionId, tokenName` | Gets the properties of the specified token. |
| `Tokens_Update` | `EXEC` | `registryName, resourceGroupName, subscriptionId, tokenName` | Updates a token with the specified parameters. |
