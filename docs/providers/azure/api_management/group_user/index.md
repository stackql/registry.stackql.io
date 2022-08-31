---
title: group_user
hide_title: false
hide_table_of_contents: false
keywords:
  - group_user
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
<tr><td><b>Name</b></td><td><code>group_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.group_user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `lastName` | `string` | Last name. |
| `registrationDate` | `string` | Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br /> |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `email` | `string` | Email address. |
| `firstName` | `string` | First name. |
| `groups` | `array` | Collection of groups user is part of. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GroupUser_List` | `SELECT` | `groupId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of user entities associated with the group. |
| `GroupUser_Create` | `INSERT` | `groupId, resourceGroupName, serviceName, subscriptionId, userId` | Add existing user to existing group |
| `GroupUser_Delete` | `DELETE` | `groupId, resourceGroupName, serviceName, subscriptionId, userId` | Remove existing user from existing group. |
| `GroupUser_CheckEntityExists` | `EXEC` | `groupId, resourceGroupName, serviceName, subscriptionId, userId` | Checks that user entity specified by identifier is associated with the group entity. |
