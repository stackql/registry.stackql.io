---
title: diagnostic_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings
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
<tr><td><b>Name</b></td><td><code>diagnostic_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.diagnostic_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | Resource location |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `marketplacePartnerId` | `string` | The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs. |
| `metrics` | `array` | The list of metric settings. |
| `eventHubName` | `string` | The name of the event hub. If none is specified, the default event hub will be selected. |
| `workspaceId` | `string` | The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2 |
| `storageAccountId` | `string` | The resource ID of the storage account to which you would like to send Diagnostic Logs. |
| `serviceBusRuleId` | `string` | The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility. |
| `eventHubAuthorizationRuleId` | `string` | The resource Id for the event hub authorization rule. |
| `logs` | `array` | The list of logs settings. |
| `logAnalyticsDestinationType` | `string` | A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type constructed as follows: &lt;normalized service identity&gt;_&lt;normalized category name&gt;. Possible values are: Dedicated and null (null is default.) |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiagnosticSettings_List` | `SELECT` | `resourceUri` | Gets the active diagnostic settings list for the specified resource. |
| `DiagnosticSettings_CreateOrUpdate` | `INSERT` | `name, resourceUri` | Creates or updates diagnostic settings for the specified resource. |
| `DiagnosticSettings_Delete` | `DELETE` | `name, resourceUri` | Deletes existing diagnostic settings for the specified resource. |
| `DiagnosticSettings_Get` | `EXEC` | `name, resourceUri` | Gets the active diagnostic settings for the specified resource. |
