---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dynatrace.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | Provisioning state of the monitoring resource |
| `liftrResourceCategory` | `string` | Liftr resource category |
| `location` | `string` | The geo-location where the resource lives |
| `planData` | `object` | Billing plan information. |
| `identity` | `object` | The properties of the managed service identities assigned to this resource. |
| `marketplaceSubscriptionStatus` | `string` | Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state. |
| `dynatraceEnvironmentProperties` | `object` | Properties of the Dynatrace environment. |
| `monitoringStatus` | `string` | Flag specifying if the resource monitoring is enabled or disabled. |
| `tags` | `object` | Resource tags. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `userInfo` | `object` | User info. |
| `liftrResourcePreference` | `integer` | The priority of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Monitors_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Monitors_ListBySubscriptionId` | `SELECT` | `subscriptionId` |
| `Monitors_CreateOrUpdate` | `INSERT` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_Delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_Get` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_GetAccountCredentials` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_GetSSODetails` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_GetVMHostPayload` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListAppServices` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListHosts` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListLinkableEnvironments` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListMonitoredResources` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_Update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
