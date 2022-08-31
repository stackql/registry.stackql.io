---
title: import_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - import_pipelines
  - container_registry
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
<tr><td><b>Name</b></td><td><code>import_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.import_pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `provisioningState` | `string` | The provisioning state of the pipeline at the time the operation was called. |
| `identity` | `object` | Managed identity for the resource. |
| `source` | `object` | The properties of the import pipeline source. |
| `options` | `array` | The list of all options configured for the pipeline. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `trigger` | `object` |  |
| `location` | `string` | The location of the import pipeline. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ImportPipelines_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all import pipelines for the specified container registry. |
| `ImportPipelines_Create` | `INSERT` | `importPipelineName, registryName, resourceGroupName, subscriptionId` | Creates an import pipeline for a container registry with the specified parameters. |
| `ImportPipelines_Delete` | `DELETE` | `importPipelineName, registryName, resourceGroupName, subscriptionId` | Deletes an import pipeline from a container registry. |
| `ImportPipelines_Get` | `EXEC` | `importPipelineName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the import pipeline. |
