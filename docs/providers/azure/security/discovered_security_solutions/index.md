---
title: discovered_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - discovered_security_solutions
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
<tr><td><b>Name</b></td><td><code>discovered_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.discovered_security_solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `offer` | `string` | The security solutions' image offer |
| `publisher` | `string` | The security solutions' image publisher |
| `securityFamily` | `string` | The security family of the discovered solution |
| `sku` | `string` | The security solutions' image sku |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Location where the resource is stored |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiscoveredSecuritySolutions_List` | `SELECT` | `api-version, subscriptionId` | Gets a list of discovered Security Solutions for the subscription. |
| `DiscoveredSecuritySolutions_ListByHomeRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Gets a list of discovered Security Solutions for the subscription and location. |
| `DiscoveredSecuritySolutions_Get` | `EXEC` | `api-version, ascLocation, discoveredSecuritySolutionName, resourceGroupName, subscriptionId` | Gets a specific discovered Security Solution. |