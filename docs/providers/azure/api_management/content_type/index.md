---
title: content_type
hide_title: false
hide_table_of_contents: false
keywords:
  - content_type
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
<tr><td><b>Name</b></td><td><code>content_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.content_type</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Content type description. |
| `schema` | `object` | Content type schema. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `version` | `string` | Content type version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContentType_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists the developer portal's content types. Content types describe content items' properties, validation rules, and constraints. |
| `ContentType_CreateOrUpdate` | `INSERT` | `contentTypeId, resourceGroupName, serviceName, subscriptionId` | Creates or updates the developer portal's content type. Content types describe content items' properties, validation rules, and constraints. Custom content types' identifiers need to start with the `c-` prefix. Built-in content types can't be modified. |
| `ContentType_Delete` | `DELETE` | `If-Match, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Removes the specified developer portal's content type. Content types describe content items' properties, validation rules, and constraints. Built-in content types (with identifiers starting with the `c-` prefix) can't be removed. |
| `ContentType_Get` | `EXEC` | `contentTypeId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the developer portal's content type. Content types describe content items' properties, validation rules, and constraints. |