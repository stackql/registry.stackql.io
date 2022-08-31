---
title: managed_instance_encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_encryption_protectors
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
<tr><td><b>Name</b></td><td><code>managed_instance_encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_encryption_protectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| `serverKeyName` | `string` | The name of the managed instance key. |
| `serverKeyType` | `string` | The encryption protector type like 'ServiceManaged', 'AzureKeyVault'. |
| `thumbprint` | `string` | Thumbprint of the server key. |
| `uri` | `string` | The URI of the server key. |
| `autoRotationEnabled` | `boolean` | Key auto rotation opt-in flag. Either true or false. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceEncryptionProtectors_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance encryption protectors |
| `ManagedInstanceEncryptionProtectors_CreateOrUpdate` | `INSERT` | `encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId` | Updates an existing encryption protector. |
| `ManagedInstanceEncryptionProtectors_Get` | `EXEC` | `encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance encryption protector. |
| `ManagedInstanceEncryptionProtectors_Revalidate` | `EXEC` | `encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId` | Revalidates an existing encryption protector. |
