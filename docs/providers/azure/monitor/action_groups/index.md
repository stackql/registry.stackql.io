---
title: action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups
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
<tr><td><b>Name</b></td><td><code>action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.action_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `voiceReceivers` | `array` | The list of voice receivers that are part of this action group. |
| `smsReceivers` | `array` | The list of SMS receivers that are part of this action group. |
| `enabled` | `boolean` | Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. |
| `azureAppPushReceivers` | `array` | The list of AzureAppPush receivers that are part of this action group. |
| `location` | `string` | Resource location |
| `tags` | `object` | Resource tags |
| `eventHubReceivers` | `array` | The list of event hub receivers that are part of this action group. |
| `armRoleReceivers` | `array` | The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported. |
| `type` | `string` | Azure resource type |
| `webhookReceivers` | `array` | The list of webhook receivers that are part of this action group. |
| `emailReceivers` | `array` | The list of email receivers that are part of this action group. |
| `logicAppReceivers` | `array` | The list of logic app receivers that are part of this action group. |
| `groupShortName` | `string` | The short name of the action group. This will be used in SMS messages. |
| `itsmReceivers` | `array` | The list of ITSM receivers that are part of this action group. |
| `automationRunbookReceivers` | `array` | The list of AutomationRunbook receivers that are part of this action group. |
| `azureFunctionReceivers` | `array` | The list of azure function receivers that are part of this action group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ActionGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of all action groups in a resource group. |
| `ActionGroups_ListBySubscriptionId` | `SELECT` | `subscriptionId` | Get a list of all action groups in a subscription. |
| `ActionGroups_CreateOrUpdate` | `INSERT` | `actionGroupName, resourceGroupName, subscriptionId` | Create a new action group or update an existing one. |
| `ActionGroups_Delete` | `DELETE` | `actionGroupName, resourceGroupName, subscriptionId` | Delete an action group. |
| `ActionGroups_CreateNotificationsAtActionGroupResourceLevel` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId, data__alertType` | Send test notifications to a set of provided receivers |
| `ActionGroups_CreateNotificationsAtResourceGroupLevel` | `EXEC` | `resourceGroupName, subscriptionId, data__alertType` | Send test notifications to a set of provided receivers |
| `ActionGroups_EnableReceiver` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId, data__receiverName` | Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers. |
| `ActionGroups_Get` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId` | Get an action group. |
| `ActionGroups_GetTestNotifications` | `EXEC` | `notificationId, subscriptionId` | Get the test notifications by the notification id |
| `ActionGroups_GetTestNotificationsAtActionGroupResourceLevel` | `EXEC` | `actionGroupName, notificationId, resourceGroupName, subscriptionId` | Get the test notifications by the notification id |
| `ActionGroups_GetTestNotificationsAtResourceGroupLevel` | `EXEC` | `notificationId, resourceGroupName, subscriptionId` | Get the test notifications by the notification id |
| `ActionGroups_PostTestNotifications` | `EXEC` | `subscriptionId, data__alertType` | Send test notifications to a set of provided receivers |
| `ActionGroups_Update` | `EXEC` | `actionGroupName, resourceGroupName, subscriptionId` | Updates an existing action group's tags. To update other fields use the CreateOrUpdate method. |
