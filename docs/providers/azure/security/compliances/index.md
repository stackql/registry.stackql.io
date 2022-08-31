---
title: compliances
hide_title: false
hide_table_of_contents: false
keywords:
  - compliances
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
<tr><td><b>Name</b></td><td><code>compliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.compliances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `resourceCount` | `integer` | The resource count of the given subscription for which the Compliance calculation was conducted (needed for Management Group Compliance calculation). |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `assessmentResult` | `array` | An array of segment, which is the actually the compliance assessment. |
| `assessmentTimestampUtcDate` | `string` | The timestamp when the Compliance calculation was conducted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Compliances_List` | `SELECT` | `api-version, scope` | The Compliance scores of the specific management group. |
| `Compliances_Get` | `EXEC` | `api-version, complianceName, scope` | Details of a specific Compliance. |
