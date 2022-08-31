---
title: iot_security_solution_analytics
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solution_analytics
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
<tr><td><b>Name</b></td><td><code>iot_security_solution_analytics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.iot_security_solution_analytics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `unhealthyDeviceCount` | `integer` | Number of unhealthy devices within your IoT Security solution. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `mostPrevalentDeviceAlerts` | `array` | List of alerts with the count of raised alerts |
| `topAlertedDevices` | `array` | List of devices with open alerts including the count of alerts per device. |
| `mostPrevalentDeviceRecommendations` | `array` | List of aggregated recommendation data, per recommendation type, per device. |
| `metrics` | `object` | IoT Security solution analytics severity metrics. |
| `devicesMetrics` | `array` | List of device metrics by the aggregation date. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotSecuritySolutionAnalytics_List` | `SELECT` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to get IoT security Analytics metrics in an array. |
| `IotSecuritySolutionAnalytics_Get` | `EXEC` | `api-version, resourceGroupName, solutionName, subscriptionId` | Use this method to get IoT Security Analytics metrics. |
