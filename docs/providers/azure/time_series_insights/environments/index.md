---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.time_series_insights.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `kind` | `string` | The kind of the environment. |
| `location` | `string` | The geo-location where the resource lives |
| `sku` | `object` | The resource model definition representing SKU |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Environments_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available environments associated with the subscription and within the specified resource group. |
| `Environments_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the available environments within a subscription, irrespective of the resource groups. |
| `Environments_CreateOrUpdate` | `INSERT` | `environmentName, resourceGroupName, subscriptionId, data__kind, data__sku` | Create or update an environment in the specified subscription and resource group. |
| `Environments_Delete` | `DELETE` | `environmentName, resourceGroupName, subscriptionId` | Deletes the environment with the specified name in the specified subscription and resource group. |
| `Environments_Get` | `EXEC` | `environmentName, resourceGroupName, subscriptionId` | Gets the environment with the specified name in the specified subscription and resource group. |
| `Environments_Update` | `EXEC` | `environmentName, resourceGroupName, subscriptionId, data__kind` | Updates the environment with the specified name in the specified subscription and resource group. |