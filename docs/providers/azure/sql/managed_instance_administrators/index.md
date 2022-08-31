---
title: managed_instance_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_administrators
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
<tr><td><b>Name</b></td><td><code>managed_instance_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_administrators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sid` | `string` | SID (object ID) of the managed instance administrator. |
| `tenantId` | `string` | Tenant ID of the managed instance administrator. |
| `administratorType` | `string` | Type of the managed instance administrator. |
| `login` | `string` | Login name of the managed instance administrator. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceAdministrators_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance administrators. |
| `ManagedInstanceAdministrators_CreateOrUpdate` | `INSERT` | `administratorName, managedInstanceName, resourceGroupName, subscriptionId` | Creates or updates a managed instance administrator. |
| `ManagedInstanceAdministrators_Delete` | `DELETE` | `administratorName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed instance administrator. |
| `ManagedInstanceAdministrators_Get` | `EXEC` | `administratorName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance administrator. |
