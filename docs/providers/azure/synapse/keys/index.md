---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - synapse
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
<tr><td><b>Id</b></td><td><code>azure.synapse.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keyVaultUrl` | `string` | The Key Vault Url of the workspace key. |
| `isActiveCMK` | `boolean` | Used to activate the workspace after a customer managed key is provided. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Keys_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Returns a list of keys in a workspace |
| `Keys_CreateOrUpdate` | `INSERT` | `keyName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace key |
| `Keys_Delete` | `DELETE` | `keyName, resourceGroupName, subscriptionId, workspaceName` | Deletes a workspace key |
| `Keys_Get` | `EXEC` | `keyName, resourceGroupName, subscriptionId, workspaceName` | Gets a workspace key |
