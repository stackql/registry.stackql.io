---
title: alert_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rules
  - monitor
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
<tr><td><b>Name</b></td><td><code>alert_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.alert_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | the name of the alert rule. |
| `description` | `string` | the description of the alert rule that will be included in the alert email. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `isEnabled` | `boolean` | the flag that indicates whether the alert rule is enabled. |
| `lastUpdatedTime` | `string` | Last time the rule was updated in ISO8601 format. |
| `type` | `string` | Azure resource type |
| `condition` | `object` | The condition that results in the alert rule being activated. |
| `action` | `object` | The action that is performed when the alert rule becomes active, and when an alert condition is resolved. |
| `provisioningState` | `string` | the provisioning state. |
| `actions` | `array` | the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved. |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AlertRules_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List the classic metric alert rules within a resource group. |
| `AlertRules_ListBySubscription` | `SELECT` | `subscriptionId` | List the classic metric alert rules within a subscription. |
| `AlertRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, ruleName, subscriptionId` | Creates or updates a classic metric alert rule. |
| `AlertRules_Delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Deletes a classic metric alert rule |
| `AlertRules_Get` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Gets a classic metric alert rule |
| `AlertRules_Update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Updates an existing classic metric AlertRuleResource. To update other fields use the CreateOrUpdate method. |
