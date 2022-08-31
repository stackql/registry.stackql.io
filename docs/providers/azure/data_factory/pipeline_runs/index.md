---
title: pipeline_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_runs
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
<tr><td><b>Name</b></td><td><code>pipeline_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.pipeline_runs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PipelineRuns_Cancel` | `EXEC` | `api-version, factoryName, resourceGroupName, runId, subscriptionId` | Cancel a pipeline run by its run ID. |
| `PipelineRuns_Get` | `EXEC` | `api-version, factoryName, resourceGroupName, runId, subscriptionId` | Get a pipeline run by its run ID. |
| `PipelineRuns_QueryByFactory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, data__lastUpdatedAfter, data__lastUpdatedBefore` | Query pipeline runs in the factory based on input filter conditions. |
