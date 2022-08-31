---
title: iot_security_solutions_analytics_recommendation
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solutions_analytics_recommendation
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
<tr><td><b>Name</b></td><td><code>iot_security_solutions_analytics_recommendation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.iot_security_solutions_analytics_recommendation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | Description of the suspected vulnerability and meaning. |
| `recommendationName` | `string` | Name of the recommendation. |
| `unhealthyDeviceCount` | `integer` | Number of unhealthy devices within the IoT Security solution. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `detectedBy` | `string` | Name of the organization that made the recommendation. |
| `healthyDevices` | `integer` | Number of healthy devices within the IoT Security solution. |
| `recommendationTypeId` | `string` | Recommendation-type GUID. |
| `tags` | `object` | Resource tags |
| `reportedSeverity` | `string` | Assessed recommendation severity. |
| `remediationSteps` | `string` | Recommended steps for remediation |
| `logAnalyticsQuery` | `string` | Log analytics query for getting the list of affected devices/alerts. |
| `recommendationDisplayName` | `string` | Display name of the recommendation type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotSecuritySolutionsAnalyticsRecommendation_List` | `SELECT` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to get the list of aggregated security analytics recommendations of yours IoT Security solution. |
| `IotSecuritySolutionsAnalyticsRecommendation_Get` | `EXEC` | `aggregatedRecommendationName, api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to get the aggregated security analytics recommendation of yours IoT Security solution. This aggregation is performed by recommendation name. |
