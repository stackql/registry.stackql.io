---
title: big_data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - big_data_pools
  - synapse
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
<tr><td><b>Name</b></td><td><code>big_data_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.big_data_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `autoPause` | `object` | Auto-pausing properties of a Big Data pool powered by Apache Spark |
| `libraryRequirements` | `object` | Library requirements for a Big Data pool powered by Apache Spark |
| `lastSucceededTimestamp` | `string` | The time when the Big Data pool was updated successfully. |
| `isComputeIsolationEnabled` | `boolean` | Whether compute isolation is required or not. |
| `defaultSparkLogFolder` | `string` | The default folder where Spark logs will be written. |
| `cacheSize` | `integer` | The cache size |
| `location` | `string` | The geo-location where the resource lives |
| `nodeCount` | `integer` | The number of nodes in the Big Data pool. |
| `autoScale` | `object` | Auto-scaling properties of a Big Data pool powered by Apache Spark |
| `sparkVersion` | `string` | The Apache Spark version. |
| `customLibraries` | `array` | List of custom libraries/packages associated with the spark pool. |
| `sparkConfigProperties` | `object` | SparkConfig Properties for a Big Data pool powered by Apache Spark |
| `nodeSize` | `string` | The level of compute power that each node in the Big Data pool has. |
| `tags` | `object` | Resource tags. |
| `sessionLevelPackagesEnabled` | `boolean` | Whether session level packages enabled. |
| `dynamicExecutorAllocation` | `object` | Dynamic Executor Allocation Properties |
| `creationDate` | `string` | The time when the Big Data pool was created. |
| `nodeSizeFamily` | `string` | The kind of nodes that the Big Data pool provides. |
| `sparkEventsFolder` | `string` | The Spark events folder |
| `provisioningState` | `string` | The state of the Big Data pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BigDataPools_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List Big Data pools in a workspace. |
| `BigDataPools_CreateOrUpdate` | `INSERT` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Create a new Big Data pool. |
| `BigDataPools_Delete` | `DELETE` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Delete a Big Data pool from the workspace. |
| `BigDataPools_Get` | `EXEC` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Get a Big Data pool. |
| `BigDataPools_Update` | `EXEC` | `bigDataPoolName, resourceGroupName, subscriptionId, workspaceName` | Patch a Big Data pool. |
