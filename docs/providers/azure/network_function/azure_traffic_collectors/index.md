---
title: azure_traffic_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_traffic_collectors
  - network_function
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
<tr><td><b>Name</b></td><td><code>azure_traffic_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_function.azure_traffic_collectors</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AzureTrafficCollectors_CreateOrUpdate` | `INSERT` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Creates or updates a Azure Traffic Collector resource |
| `AzureTrafficCollectors_Delete` | `DELETE` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Deletes a specified Azure Traffic Collector resource. |
| `AzureTrafficCollectors_Get` | `EXEC` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Gets the specified Azure Traffic Collector in a specified resource group |
| `AzureTrafficCollectors_UpdateTags` | `EXEC` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Updates the specified Azure Traffic Collector tags. |
