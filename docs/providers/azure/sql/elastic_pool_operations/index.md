---
title: elastic_pool_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pool_operations
  - sql
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
<tr><td><b>Name</b></td><td><code>elastic_pool_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.elastic_pool_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The operation description. |
| `isUserError` | `boolean` | Whether or not the error is a user error. |
| `estimatedCompletionTime` | `string` | The estimated completion time of the operation. |
| `isCancellable` | `boolean` | Whether the operation can be cancelled. |
| `percentComplete` | `integer` | The percentage of the operation completed. |
| `serverName` | `string` | The name of the server. |
| `state` | `string` | The operation state. |
| `operation` | `string` | The name of operation. |
| `elasticPoolName` | `string` | The name of the elastic pool the operation is being performed on. |
| `startTime` | `string` | The operation start time. |
| `errorCode` | `integer` | The operation error code. |
| `errorDescription` | `string` | The operation error description. |
| `operationFriendlyName` | `string` | The friendly name of operation. |
| `errorSeverity` | `integer` | The operation error severity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ElasticPoolOperations_ListByElasticPool` | `SELECT` | `elasticPoolName, resourceGroupName, serverName, subscriptionId` | Gets a list of operations performed on the elastic pool. |
| `ElasticPoolOperations_Cancel` | `EXEC` | `elasticPoolName, operationId, resourceGroupName, serverName, subscriptionId` | Cancels the asynchronous operation on the elastic pool. |
