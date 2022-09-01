---
title: activity_log_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - activity_log_alerts
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
<tr><td><b>Name</b></td><td><code>activity_log_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.activity_log_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `description` | `string` | A description of this Activity Log Alert rule. |
| `condition` | `object` | An Activity Log Alert rule condition that is met when all its member conditions are met. |
| `scopes` | `array` | A list of resource IDs that will be used as prefixes. The alert will only apply to Activity Log events with resource IDs that fall under one of these prefixes. This list must include at least one item. |
| `type` | `string` | Azure resource type |
| `enabled` | `boolean` | Indicates whether this Activity Log Alert rule is enabled. If an Activity Log Alert rule is not enabled, then none of its actions will be activated. |
| `actions` | `object` | A list of Activity Log Alert rule actions. |
| `tags` | `object` | Resource tags |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ActivityLogAlerts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of all Activity Log Alert rules in a resource group. |
| `ActivityLogAlerts_ListBySubscriptionId` | `SELECT` | `subscriptionId` | Get a list of all Activity Log Alert rules in a subscription. |
| `ActivityLogAlerts_CreateOrUpdate` | `INSERT` | `activityLogAlertName, resourceGroupName, subscriptionId` | Create a new Activity Log Alert rule or update an existing one. |
| `ActivityLogAlerts_Delete` | `DELETE` | `activityLogAlertName, resourceGroupName, subscriptionId` | Delete an Activity Log Alert rule. |
| `ActivityLogAlerts_Get` | `EXEC` | `activityLogAlertName, resourceGroupName, subscriptionId` | Get an Activity Log Alert rule. |
| `ActivityLogAlerts_Update` | `EXEC` | `activityLogAlertName, resourceGroupName, subscriptionId` | Updates 'tags' and 'enabled' fields in an existing Alert rule. This method is used to update the Alert rule tags, and to enable or disable the Alert rule. To update other fields use CreateOrUpdate operation. |
