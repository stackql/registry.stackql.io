---
title: configuration_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_assignments
  - maintenance
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
<tr><td><b>Name</b></td><td><code>configuration_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.configuration_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `maintenanceConfigurationId` | `string` | The maintenance configuration Id |
| `resourceId` | `string` | The unique resourceId |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Location of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConfigurationAssignments_List` | `SELECT` | `providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | List configurationAssignments for resource. |
| `ConfigurationAssignments_CreateOrUpdate` | `INSERT` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Register configuration for resource. |
| `ConfigurationAssignments_Delete` | `DELETE` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Unregister configuration for resource. |
| `ConfigurationAssignments_CreateOrUpdateParent` | `EXEC` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Register configuration for resource. |
| `ConfigurationAssignments_DeleteParent` | `EXEC` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Unregister configuration for resource. |
| `ConfigurationAssignments_Get` | `EXEC` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Get configuration for resource. |
| `ConfigurationAssignments_GetParent` | `EXEC` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Get configuration for resource. |
| `ConfigurationAssignments_ListParent` | `EXEC` | `providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | List configurationAssignments for resource. |