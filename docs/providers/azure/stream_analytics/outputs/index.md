---
title: outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - outputs
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.outputs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `datasource` | `object` | Describes the data source that output will be written to. |
| `etag` | `string` | The current entity tag for the output. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| `sizeWindow` | `number` | The size window to constrain a Stream Analytics output to. |
| `type` | `string` | Resource type |
| `diagnostics` | `object` | Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention. |
| `serialization` | `object` | Describes how data from an input is serialized or how data is serialized when written to an output. |
| `timeWindow` | `string` | The time frame for filtering Stream Analytics job outputs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Outputs_ListByStreamingJob` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Lists all of the outputs under the specified streaming job. |
| `Outputs_CreateOrReplace` | `INSERT` | `jobName, outputName, resourceGroupName, subscriptionId` | Creates an output or replaces an already existing output under an existing streaming job. |
| `Outputs_Delete` | `DELETE` | `jobName, outputName, resourceGroupName, subscriptionId` | Deletes an output from the streaming job. |
| `Outputs_Get` | `EXEC` | `jobName, outputName, resourceGroupName, subscriptionId` | Gets details about the specified output. |
| `Outputs_Test` | `EXEC` | `jobName, outputName, resourceGroupName, subscriptionId` | Tests whether an output’s datasource is reachable and usable by the Azure Stream Analytics service. |
| `Outputs_Update` | `EXEC` | `jobName, outputName, resourceGroupName, subscriptionId` | Updates an existing output under an existing streaming job. This can be used to partially update (ie. update one or two properties) an output without affecting the rest the job or output definition. |
