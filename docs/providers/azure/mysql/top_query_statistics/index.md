---
title: top_query_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - top_query_statistics
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
<tr><td><b>Name</b></td><td><code>top_query_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.top_query_statistics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `queryExecutionCount` | `integer` | Number of query executions in this time interval. |
| `aggregationFunction` | `string` | Aggregation function name. |
| `endTime` | `string` | Observation end time. |
| `metricValueUnit` | `string` | Metric value unit. |
| `startTime` | `string` | Observation start time. |
| `queryId` | `string` | Database query identifier. |
| `databaseNames` | `array` | The list of database names. |
| `metricDisplayName` | `string` | Metric display name. |
| `metricValue` | `number` | Metric value. |
| `metricName` | `string` | Metric name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TopQueryStatistics_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Retrieve the Query-Store top queries for specified metric and aggregation. |
| `TopQueryStatistics_Get` | `EXEC` | `queryStatisticId, resourceGroupName, serverName, subscriptionId` | Retrieve the query statistic for specified identifier. |
