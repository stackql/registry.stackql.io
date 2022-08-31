---
title: governance_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_rule
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
<tr><td><b>Name</b></td><td><code>governance_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.governance_rule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | description of the governanceRule |
| `conditionSets` | `array` | The governance rule conditionSets - see examples |
| `ruleType` | `string` | The rule type of the governance rule, defines the source of the rule e.g. Integrated |
| `isGracePeriod` | `boolean` | Defines whether there is a grace period on the governance rule |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `displayName` | `string` | display name of the governanceRule |
| `sourceResourceType` | `string` | The governance rule source, what the rule affects, e.g. Assessments |
| `isDisabled` | `boolean` | Defines whether the rule is active/inactive |
| `remediationTimeframe` | `string` | Governance rule remediation timeframe - this is the time that will affect on the grace-period duration e.g. 7.00:00:00 - means 7 days |
| `ownerSource` | `object` | Describe the owner source of governance rule |
| `rulePriority` | `integer` | The governance rule priority, priority to the lower number. Rules with the same priority on the same subscription will not be allowed |
| `governanceEmailNotification` | `object` | The governance email weekly notification configuration. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `GovernanceRule_List` | `SELECT` | `api-version, subscriptionId` |
