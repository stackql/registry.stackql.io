---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - kubernetes_configuration
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
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.kubernetes_configuration.operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID for the async operation. |
| `name` | `string` | Name of the async operation. |
| `properties` | `object` | Additional information, if available. |
| `status` | `string` | Operation status. |
| `error` | `object` | The error detail. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OperationStatus_List` | `SELECT` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId` | List Async Operations, currently in progress, in a cluster |
| `OperationStatus_Get` | `EXEC` | `clusterName, clusterResourceName, clusterRp, extensionName, operationId, resourceGroupName, subscriptionId` | Get Async Operation status |