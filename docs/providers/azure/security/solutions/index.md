---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - security
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
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Location where the resource is stored |
| `protectionStatus` | `string` | The security solutions' status |
| `provisioningState` | `string` | The security family provisioning State |
| `securityFamily` | `string` | The security family of the security solution |
| `template` | `string` | The security solutions' template |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecuritySolutions_List` | `SELECT` | `api-version, subscriptionId` | Gets a list of Security Solutions for the subscription. |
| `SecuritySolutions_Get` | `EXEC` | `api-version, ascLocation, resourceGroupName, securitySolutionName, subscriptionId` | Gets a specific Security Solution. |