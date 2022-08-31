---
title: secure_score_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - secure_score_controls
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
<tr><td><b>Name</b></td><td><code>secure_score_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.secure_score_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `score` | `object` | Calculation result data |
| `notApplicableResourceCount` | `integer` | Number of not applicable resources in the control |
| `weight` | `integer` | The relative weight for this specific control in each of your subscriptions. Used when calculating an aggregated score for this control across all of your subscriptions. |
| `healthyResourceCount` | `integer` | Number of healthy resources in the control |
| `unhealthyResourceCount` | `integer` | Number of unhealthy resources in the control |
| `definition` | `object` | Information about the security control. |
| `displayName` | `string` | User friendly display name of the control |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecureScoreControls_List` | `SELECT` | `api-version, subscriptionId` | Get all security controls within a scope |
| `SecureScoreControls_ListBySecureScore` | `SELECT` | `api-version, secureScoreName, subscriptionId` | Get all security controls for a specific initiative within a scope |
