---
title: metric_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts
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
<tr><td><b>Name</b></td><td><code>metric_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `description` | `string` | the description of the metric alert that will be included in the alert email. |
| `windowSize` | `string` | the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. |
| `targetResourceType` | `string` | the resource type of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource. |
| `scopes` | `array` | the list of resource id's that this metric alert is scoped to. |
| `enabled` | `boolean` | the flag that indicates whether the metric alert is enabled. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `evaluationFrequency` | `string` | how often the metric alert is evaluated represented in ISO 8601 duration format. |
| `criteria` | `object` | The rule criteria that defines the conditions of the alert rule. |
| `location` | `string` | Resource location |
| `targetResourceRegion` | `string` | the region of the target resource(s) on which the alert is created/updated. Mandatory if the scope contains a subscription, resource group, or more than one resource. |
| `actions` | `array` | the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved. |
| `isMigrated` | `boolean` | the value indicating whether this alert rule is migrated. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `severity` | `integer` | Alert severity {0, 1, 2, 3, 4} |
| `lastUpdatedTime` | `string` | Last time the rule was updated in ISO8601 format. |
| `type` | `string` | Azure resource type |
| `autoMitigate` | `boolean` | the flag that indicates whether the alert should be auto resolved or not. The default is true. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MetricAlerts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve alert rule definitions in a resource group. |
| `MetricAlerts_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve alert rule definitions in a subscription. |
| `MetricAlerts_CreateOrUpdate` | `INSERT` | `resourceGroupName, ruleName, subscriptionId` | Create or update an metric alert definition. |
| `MetricAlerts_Delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Delete an alert rule definition. |
| `MetricAlerts_Get` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Retrieve an alert rule definition. |
| `MetricAlerts_Update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Update an metric alert definition. |
