---
title: connector_governance_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_governance_rule
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
<tr><td><b>Name</b></td><td><code>connector_governance_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.connector_governance_rule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | description of the governanceRule |
| `isDisabled` | `boolean` | Defines whether the rule is active/inactive |
| `remediationTimeframe` | `string` | Governance rule remediation timeframe - this is the time that will affect on the grace-period duration e.g. 7.00:00:00 - means 7 days |
| `rulePriority` | `integer` | The governance rule priority, priority to the lower number. Rules with the same priority on the same subscription will not be allowed |
| `displayName` | `string` | display name of the governanceRule |
| `ruleType` | `string` | The rule type of the governance rule, defines the source of the rule e.g. Integrated |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `sourceResourceType` | `string` | The governance rule source, what the rule affects, e.g. Assessments |
| `conditionSets` | `array` | The governance rule conditionSets - see examples |
| `ownerSource` | `object` | Describe the owner source of governance rule |
| `governanceEmailNotification` | `object` | The governance email weekly notification configuration. |
| `isGracePeriod` | `boolean` | Defines whether there is a grace period on the governance rule |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SecurityConnectorGovernanceRule_List` | `SELECT` | `api-version, resourceGroupName, securityConnectorName, subscriptionId` |
