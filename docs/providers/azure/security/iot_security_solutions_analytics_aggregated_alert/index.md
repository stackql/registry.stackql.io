---
title: iot_security_solutions_analytics_aggregated_alert
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solutions_analytics_aggregated_alert
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
<tr><td><b>Name</b></td><td><code>iot_security_solutions_analytics_aggregated_alert</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.iot_security_solutions_analytics_aggregated_alert</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Description of the suspected vulnerability and meaning. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `alertType` | `string` | Name of the alert type. |
| `systemSource` | `string` | The type of the alerted resource (Azure, Non-Azure). |
| `tags` | `object` | Resource tags |
| `count` | `integer` | Number of alerts occurrences within the aggregated time window. |
| `vendorName` | `string` | Name of the organization that raised the alert. |
| `logAnalyticsQuery` | `string` | Log analytics query for getting the list of affected devices/alerts. |
| `actionTaken` | `string` | IoT Security solution alert response. |
| `topDevicesList` | `array` | 10 devices with the highest number of occurrences of this alert type, on this day. |
| `effectedResourceType` | `string` | Azure resource ID of the resource that received the alerts. |
| `reportedSeverity` | `string` | Assessed alert severity. |
| `remediationSteps` | `string` | Recommended steps for remediation. |
| `aggregatedDateUtc` | `string` | Date of detection. |
| `alertDisplayName` | `string` | Display name of the alert type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotSecuritySolutionsAnalyticsAggregatedAlert_List` | `SELECT` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to get the aggregated alert list of yours IoT Security solution. |
| `IotSecuritySolutionsAnalyticsAggregatedAlert_Dismiss` | `EXEC` | `aggregatedAlertName, api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to dismiss an aggregated IoT Security Solution Alert. |
| `IotSecuritySolutionsAnalyticsAggregatedAlert_Get` | `EXEC` | `aggregatedAlertName, api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name. |
