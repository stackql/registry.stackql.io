---
title: sql_pool_workload_classifier
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_workload_classifier
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
<tr><td><b>Name</b></td><td><code>sql_pool_workload_classifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_workload_classifier</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `startTime` | `string` | The workload classifier start time for classification. |
| `context` | `string` | The workload classifier context. |
| `endTime` | `string` | The workload classifier end time for classification. |
| `importance` | `string` | The workload classifier importance. |
| `label` | `string` | The workload classifier label. |
| `memberName` | `string` | The workload classifier member name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolWorkloadClassifier_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Get list of  Sql pool's workload classifier for workload groups. |
| `SqlPoolWorkloadClassifier_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName` | Create Or Update workload classifier for a Sql pool's workload group. |
| `SqlPoolWorkloadClassifier_Delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName` | Remove workload classifier of a Sql pool's workload group. |
| `SqlPoolWorkloadClassifier_Get` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName` | Get a workload classifier of Sql pool's workload group. |