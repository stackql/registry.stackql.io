---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.extensions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Extensions_Create` | `INSERT` | `clusterName, extensionName, resourceGroupName, subscriptionId` | Creates an HDInsight cluster extension. |
| `Extensions_Delete` | `DELETE` | `clusterName, extensionName, resourceGroupName, subscriptionId` | Deletes the specified extension for HDInsight cluster. |
| `Extensions_DisableAzureMonitor` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Disables the Azure Monitor on the HDInsight cluster. |
| `Extensions_DisableMonitoring` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Disables the Operations Management Suite (OMS) on the HDInsight cluster. |
| `Extensions_EnableAzureMonitor` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Enables the Azure Monitor on the HDInsight cluster. |
| `Extensions_EnableMonitoring` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Enables the Operations Management Suite (OMS) on the HDInsight cluster. |
| `Extensions_Get` | `EXEC` | `clusterName, extensionName, resourceGroupName, subscriptionId` | Gets the extension properties for the specified HDInsight cluster extension. |
| `Extensions_GetAzureAsyncOperationStatus` | `EXEC` | `clusterName, extensionName, operationId, resourceGroupName, subscriptionId` | Gets the async operation status. |
| `Extensions_GetAzureMonitorStatus` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets the status of Azure Monitor on the HDInsight cluster. |
| `Extensions_GetMonitoringStatus` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets the status of Operations Management Suite (OMS) on the HDInsight cluster. |
