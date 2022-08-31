---
title: application_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - application_security_groups
  - network
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
<tr><td><b>Name</b></td><td><code>application_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `provisioningState` | `string` | The current provisioning state. |
| `resourceGuid` | `string` | The resource GUID property of the application security group resource. It uniquely identifies a resource, even if the user changes its name or migrate the resource across subscriptions or resource groups. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationSecurityGroups_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the application security groups in a resource group. |
| `ApplicationSecurityGroups_ListAll` | `SELECT` | `subscriptionId` | Gets all application security groups in a subscription. |
| `ApplicationSecurityGroups_CreateOrUpdate` | `INSERT` | `applicationSecurityGroupName, resourceGroupName, subscriptionId` | Creates or updates an application security group. |
| `ApplicationSecurityGroups_Delete` | `DELETE` | `applicationSecurityGroupName, resourceGroupName, subscriptionId` | Deletes the specified application security group. |
| `ApplicationSecurityGroups_Get` | `EXEC` | `applicationSecurityGroupName, resourceGroupName, subscriptionId` | Gets information about the specified application security group. |
| `ApplicationSecurityGroups_UpdateTags` | `EXEC` | `applicationSecurityGroupName, resourceGroupName, subscriptionId` | Updates an application security group's tags. |
