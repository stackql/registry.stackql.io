---
title: alerts_suppression_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_suppression_rules
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
<tr><td><b>Name</b></td><td><code>alerts_suppression_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.alerts_suppression_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `alertType` | `string` | Type of the alert to automatically suppress. For all alert types, use '*' |
| `expirationDateUtc` | `string` | Expiration date of the rule, if value is not provided or provided as null this field will default to the maximum allowed expiration date. |
| `state` | `string` | Possible states of the rule |
| `suppressionAlertsScope` | `object` |  |
| `comment` | `string` | Any comment regarding the rule |
| `lastModifiedUtc` | `string` | The last time this rule was modified |
| `reason` | `string` | The reason for dismissing the alert |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AlertsSuppressionRules_List` | `SELECT` | `api-version, subscriptionId` | List of all the dismiss rules for the given subscription |
| `AlertsSuppressionRules_Delete` | `DELETE` | `alertsSuppressionRuleName, api-version, subscriptionId` | Delete dismiss alert rule for this subscription. |
| `AlertsSuppressionRules_Get` | `EXEC` | `alertsSuppressionRuleName, api-version, subscriptionId` | Get dismiss rule, with name: {alertsSuppressionRuleName}, for the given subscription |
| `AlertsSuppressionRules_Update` | `EXEC` | `alertsSuppressionRuleName, api-version, subscriptionId` | Update existing rule or create new rule if it doesn't exist |
