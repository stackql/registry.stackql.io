---
title: wait_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - wait_statistics
  - mysql
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
<tr><td><b>Name</b></td><td><code>wait_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.wait_statistics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `startTime` | `string` | Observation start time. |
| `userId` | `integer` | Database user identifier. |
| `eventTypeName` | `string` | Wait event type name. |
| `databaseName` | `string` | Database Name. |
| `endTime` | `string` | Observation end time. |
| `eventName` | `string` | Wait event name. |
| `queryId` | `integer` | Database query identifier. |
| `totalTimeInMs` | `number` | Total time of wait in milliseconds in this time interval. |
| `count` | `integer` | Wait event count observed in this time interval. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WaitStatistics_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Retrieve wait statistics for specified aggregation window. |
| `WaitStatistics_Get` | `EXEC` | `resourceGroupName, serverName, subscriptionId, waitStatisticsId` | Retrieve wait statistics for specified identifier. |
