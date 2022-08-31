---
title: workload_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_classifiers
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
<tr><td><b>Name</b></td><td><code>workload_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.workload_classifiers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `label` | `string` | The workload classifier label. |
| `memberName` | `string` | The workload classifier member name. |
| `startTime` | `string` | The workload classifier start time for classification. |
| `context` | `string` | The workload classifier context. |
| `endTime` | `string` | The workload classifier end time for classification. |
| `importance` | `string` | The workload classifier importance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkloadClassifiers_ListByWorkloadGroup` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Gets the list of workload classifiers for a workload group |
| `WorkloadClassifiers_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName` | Creates or updates a workload classifier. |
| `WorkloadClassifiers_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName` | Deletes a workload classifier. |
| `WorkloadClassifiers_Get` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName` | Gets a workload classifier |
