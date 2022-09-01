---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - data_factory
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
<tr><td><b>Id</b></td><td><code>azure.data_factory.pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `description` | `string` | The description of the pipeline. |
| `etag` | `string` | Etag identifies change in the resource. |
| `policy` | `object` | Pipeline Policy. |
| `variables` | `object` | Definition of variable for a Pipeline. |
| `activities` | `array` | List of activities in pipeline. |
| `parameters` | `object` | Definition of all parameters for an entity. |
| `runDimensions` | `object` | Dimensions emitted by Pipeline. |
| `folder` | `object` | The folder that this Pipeline is in. If not specified, Pipeline will appear at the root level. |
| `type` | `string` | The resource type. |
| `concurrency` | `integer` | The max number of concurrent runs for the pipeline. |
| `annotations` | `array` | List of tags that can be used for describing the Pipeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pipelines_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists pipelines. |
| `Pipelines_CreateOrUpdate` | `INSERT` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Creates or updates a pipeline. |
| `Pipelines_Delete` | `DELETE` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Deletes a pipeline. |
| `Pipelines_CreateRun` | `EXEC` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Creates a run of a pipeline. |
| `Pipelines_Get` | `EXEC` | `api-version, factoryName, pipelineName, resourceGroupName, subscriptionId` | Gets a pipeline. |
