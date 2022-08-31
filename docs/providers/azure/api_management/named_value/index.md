---
title: named_value
hide_title: false
hide_table_of_contents: false
keywords:
  - named_value
  - api_management
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
<tr><td><b>Name</b></td><td><code>named_value</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.named_value</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `displayName` | `string` | Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters. |
| `keyVault` | `object` | KeyVault contract details. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `value` | `string` | Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NamedValue_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of named values defined within a service instance. |
| `NamedValue_CreateOrUpdate` | `INSERT` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Creates or updates named value. |
| `NamedValue_Delete` | `DELETE` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId` | Deletes specific named value from the API Management service instance. |
| `NamedValue_Get` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the named value specified by its identifier. |
| `NamedValue_GetEntityTag` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the named value specified by its identifier. |
| `NamedValue_ListValue` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the secret of the named value specified by its identifier. |
| `NamedValue_RefreshSecret` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Refresh the secret of the named value specified by its identifier. |
| `NamedValue_Update` | `EXEC` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId` | Updates the specific named value. |