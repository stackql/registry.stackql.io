---
title: scheduled_query_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query_rules
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
<tr><td><b>Name</b></td><td><code>scheduled_query_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.scheduled_query_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `description` | `string` | The description of the Log Search rule. |
| `enabled` | `string` | The flag which indicates whether the Log Search rule is enabled. Value should be true or false |
| `autoMitigate` | `boolean` | The flag that indicates whether the alert should be automatically resolved or not. The default is false. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `displayName` | `string` | The display name of the alert rule |
| `type` | `string` | Azure resource type |
| `action` | `object` | Action descriptor. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `source` | `object` | Specifies the log search query. |
| `provisioningState` | `string` | Provisioning state of the scheduled query rule |
| `schedule` | `object` | Defines how often to run the search and the time interval. |
| `lastUpdatedTime` | `string` | Last time the rule was updated in IS08601 format. |
| `location` | `string` | Resource location |
| `isLegacyLogAnalyticsRule` | `boolean` | True if alert rule is legacy Log Analytic rule |
| `createdWithApiVersion` | `string` | The api-version used when creating this alert rule |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScheduledQueryRules_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List the Log Search rules within a resource group. |
| `ScheduledQueryRules_ListBySubscription` | `SELECT` | `subscriptionId` | List the Log Search rules within a subscription group. |
| `ScheduledQueryRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, ruleName, subscriptionId` | Creates or updates an log search rule. |
| `ScheduledQueryRules_Delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Deletes a Log Search rule |
| `ScheduledQueryRules_Get` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Gets an Log Search rule |
| `ScheduledQueryRules_Update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Update log search Rule. |
