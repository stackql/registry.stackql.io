---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
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
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Group description. Can contain HTML formatting tags. |
| `builtIn` | `boolean` | true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false. |
| `displayName` | `string` | Group name. |
| `externalId` | `string` | For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group object id&gt;`; otherwise the value is null. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Group_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of groups defined within a service instance. |
| `Group_CreateOrUpdate` | `INSERT` | `groupId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a group. |
| `Group_Delete` | `DELETE` | `If-Match, groupId, resourceGroupName, serviceName, subscriptionId` | Deletes specific group of the API Management service instance. |
| `Group_Get` | `EXEC` | `groupId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the group specified by its identifier. |
| `Group_GetEntityTag` | `EXEC` | `groupId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the group specified by its identifier. |
| `Group_Update` | `EXEC` | `If-Match, groupId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the group specified by its identifier. |
