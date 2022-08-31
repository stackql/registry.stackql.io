---
title: diagnostic
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic
  - api_management
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
<tr><td><b>Name</b></td><td><code>diagnostic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.diagnostic</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `verbosity` | `string` | The verbosity level applied to traces emitted by trace policies. |
| `operationNameFormat` | `string` | The format of the Operation Name for Application Insights telemetries. Default is Name. |
| `sampling` | `object` | Sampling settings for Diagnostic. |
| `logClientIp` | `boolean` | Log the ClientIP. Default is false. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `alwaysLog` | `string` | Specifies for what type of messages sampling settings should not apply. |
| `frontend` | `object` | Diagnostic settings for incoming/outgoing HTTP messages to the Gateway. |
| `httpCorrelationProtocol` | `string` | Sets correlation protocol to use for Application Insights diagnostics. |
| `loggerId` | `string` | Resource Id of a target logger. |
| `backend` | `object` | Diagnostic settings for incoming/outgoing HTTP messages to the Gateway. |
| `metrics` | `boolean` | Emit custom metrics via emit-metric policy. Applicable only to Application Insights diagnostic settings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Diagnostic_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all diagnostics of the API Management service instance. |
| `Diagnostic_CreateOrUpdate` | `INSERT` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Creates a new Diagnostic or updates an existing one. |
| `Diagnostic_Delete` | `DELETE` | `If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Diagnostic. |
| `Diagnostic_Get` | `EXEC` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Diagnostic specified by its identifier. |
| `Diagnostic_GetEntityTag` | `EXEC` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Diagnostic specified by its identifier. |
| `Diagnostic_Update` | `EXEC` | `If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the Diagnostic specified by its identifier. |