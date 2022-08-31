---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - devops
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
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.devops.pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `project` | `object` | Reference to an Azure DevOps Project. |
| `tags` | `object` | Resource Tags |
| `location` | `string` | Resource Location |
| `organization` | `object` | Reference to an Azure DevOps Organization. |
| `bootstrapConfiguration` | `object` | Configuration used to bootstrap a Pipeline. |
| `type` | `string` | Resource Type |
| `pipelineId` | `integer` | Unique identifier of the Azure Pipeline within the Azure DevOps Project. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pipelines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Azure Pipelines under the specified resource group. |
| `Pipelines_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all Azure Pipelines under the specified subscription. |
| `Pipelines_CreateOrUpdate` | `INSERT` | `pipelineName, resourceGroupName, subscriptionId` | Creates or updates an Azure Pipeline. |
| `Pipelines_Delete` | `DELETE` | `pipelineName, resourceGroupName, subscriptionId` | Deletes an Azure Pipeline. |
| `Pipelines_Get` | `EXEC` | `pipelineName, resourceGroupName, subscriptionId` | Gets an existing Azure Pipeline. |
| `Pipelines_Update` | `EXEC` | `pipelineName, resourceGroupName, subscriptionId` | Updates the properties of an Azure Pipeline. Currently, only tags can be updated. |
