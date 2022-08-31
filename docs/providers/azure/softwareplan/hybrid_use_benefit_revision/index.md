---
title: hybrid_use_benefit_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_use_benefit_revision
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
<tr><td><b>Name</b></td><td><code>hybrid_use_benefit_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.softwareplan.hybrid_use_benefit_revision</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `lastUpdatedDate` | `string` | Last updated date |
| `provisioningState` | `string` | Represent the current state of the Reservation. |
| `sku` | `object` | The SKU to be applied for this resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `createdDate` | `string` | Created date |
| `etag` | `integer` | Indicates the revision of the hybrid use benefit |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `HybridUseBenefitRevision_List` | `SELECT` | `planId, scope` |
