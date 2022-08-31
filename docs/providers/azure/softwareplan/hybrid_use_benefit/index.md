---
title: hybrid_use_benefit
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_use_benefit
  - softwareplan
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
<tr><td><b>Name</b></td><td><code>hybrid_use_benefit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.softwareplan.hybrid_use_benefit</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `provisioningState` | `string` | Represent the current state of the Reservation. |
| `sku` | `object` | The SKU to be applied for this resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `createdDate` | `string` | Created date |
| `etag` | `integer` | Indicates the revision of the hybrid use benefit |
| `lastUpdatedDate` | `string` | Last updated date |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridUseBenefit_List` | `SELECT` | `scope` | Get all hybrid use benefits associated with an ARM resource. |
| `HybridUseBenefit_Create` | `INSERT` | `planId, scope, data__sku` | Create a new hybrid use benefit under a given scope |
| `HybridUseBenefit_Delete` | `DELETE` | `planId, scope` | Deletes a given plan ID |
| `HybridUseBenefit_Get` | `EXEC` | `planId, scope` | Gets a given plan ID |
| `HybridUseBenefit_Update` | `EXEC` | `planId, scope, data__sku` | Updates an existing hybrid use benefit |
