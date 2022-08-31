---
title: quota_by_period_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_by_period_keys
  - api_management
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
<tr><td><b>Name</b></td><td><code>quota_by_period_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.quota_by_period_keys</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `QuotaByPeriodKeys_Get` | `EXEC` | `quotaCounterKey, quotaPeriodKey, resourceGroupName, serviceName, subscriptionId` | Gets the value of the quota counter associated with the counter-key in the policy for the specific period in service instance. |
| `QuotaByPeriodKeys_Update` | `EXEC` | `quotaCounterKey, quotaPeriodKey, resourceGroupName, serviceName, subscriptionId` | Updates an existing quota counter value in the specified service instance. |
