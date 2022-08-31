---
title: managed_instance_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_keys
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
<tr><td><b>Name</b></td><td><code>managed_instance_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `thumbprint` | `string` | Thumbprint of the key. |
| `uri` | `string` | The URI of the key. If the ServerKeyType is AzureKeyVault, then the URI is required. |
| `autoRotationEnabled` | `boolean` | Key auto rotation opt-in flag. Either true or false. |
| `creationDate` | `string` | The key creation date. |
| `kind` | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| `serverKeyType` | `string` | The key type like 'ServiceManaged', 'AzureKeyVault'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceKeys_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance keys. |
| `ManagedInstanceKeys_CreateOrUpdate` | `INSERT` | `keyName, managedInstanceName, resourceGroupName, subscriptionId` | Creates or updates a managed instance key. |
| `ManagedInstanceKeys_Delete` | `DELETE` | `keyName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes the managed instance key with the given name. |
| `ManagedInstanceKeys_Get` | `EXEC` | `keyName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance key. |