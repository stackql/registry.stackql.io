---
title: file_services
hide_title: false
hide_table_of_contents: false
keywords:
  - file_services
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
<tr><td><b>Name</b></td><td><code>file_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.file_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `properties` | `` | The properties of File services in storage account. |
| `sku` | `object` | The resource model definition representing SKU |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FileServices_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all file services in storage accounts |
| `FileServices_GetServiceProperties` | `EXEC` | `FileServicesName, accountName, resourceGroupName, subscriptionId` | Gets the properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules. |
| `FileServices_SetServiceProperties` | `EXEC` | `FileServicesName, accountName, resourceGroupName, subscriptionId` | Sets the properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules.  |
