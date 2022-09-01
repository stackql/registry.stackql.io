---
title: logger
hide_title: false
hide_table_of_contents: false
keywords:
  - logger
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
<tr><td><b>Name</b></td><td><code>logger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.logger</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `description` | `string` | Logger description. |
| `credentials` | `object` | The name and SendRule connection string of the event hub for azureEventHub logger.<br />Instrumentation key for applicationInsights logger. |
| `isBuffered` | `boolean` | Whether records are buffered in the logger before publishing. Default is assumed to be true. |
| `loggerType` | `string` | Logger type. |
| `resourceId` | `string` | Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource). |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Logger_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of loggers in the specified service instance. |
| `Logger_CreateOrUpdate` | `INSERT` | `loggerId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a logger. |
| `Logger_Delete` | `DELETE` | `If-Match, loggerId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified logger. |
| `Logger_Get` | `EXEC` | `loggerId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the logger specified by its identifier. |
| `Logger_GetEntityTag` | `EXEC` | `loggerId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the logger specified by its identifier. |
| `Logger_Update` | `EXEC` | `If-Match, loggerId, resourceGroupName, serviceName, subscriptionId` | Updates an existing logger. |
