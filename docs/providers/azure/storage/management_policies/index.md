---
title: management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - management_policies
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
<tr><td><b>Name</b></td><td><code>management_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.management_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementPolicies_CreateOrUpdate` | `INSERT` | `accountName, managementPolicyName, resourceGroupName, subscriptionId` | Sets the managementpolicy to the specified storage account. |
| `ManagementPolicies_Delete` | `DELETE` | `accountName, managementPolicyName, resourceGroupName, subscriptionId` | Deletes the managementpolicy associated with the specified storage account. |
| `ManagementPolicies_Get` | `EXEC` | `accountName, managementPolicyName, resourceGroupName, subscriptionId` | Gets the managementpolicy associated with the specified storage account. |
