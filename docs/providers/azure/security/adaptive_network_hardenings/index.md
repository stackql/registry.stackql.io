---
title: adaptive_network_hardenings
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_network_hardenings
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
<tr><td><b>Name</b></td><td><code>adaptive_network_hardenings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.adaptive_network_hardenings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `rulesCalculationTime` | `string` | The UTC time on which the rules were calculated |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `effectiveNetworkSecurityGroups` | `array` | The Network Security Groups effective on the network interfaces of the protected resource |
| `rules` | `array` | The security rules which are recommended to be effective on the VM |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AdaptiveNetworkHardenings_ListByExtendedResource` | `SELECT` | `api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId` | Gets a list of Adaptive Network Hardenings resources in scope of an extended resource. |
| `AdaptiveNetworkHardenings_Enforce` | `EXEC` | `adaptiveNetworkHardeningEnforceAction, adaptiveNetworkHardeningResourceName, api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId, data__networkSecurityGroups, data__rules` | Enforces the given rules on the NSG(s) listed in the request |
| `AdaptiveNetworkHardenings_Get` | `EXEC` | `adaptiveNetworkHardeningResourceName, api-version, resourceGroupName, resourceName, resourceNamespace, resourceType, subscriptionId` | Gets a single Adaptive Network Hardening resource |