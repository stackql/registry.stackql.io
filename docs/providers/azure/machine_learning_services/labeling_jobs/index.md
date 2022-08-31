---
title: labeling_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - labeling_jobs
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>labeling_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.labeling_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Labeling job definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LabelingJobs_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `LabelingJobs_CreateOrUpdate` | `INSERT` | `id, resourceGroupName, subscriptionId, workspaceName, data__properties` |
| `LabelingJobs_Delete` | `DELETE` | `id, resourceGroupName, subscriptionId, workspaceName` |
| `LabelingJobs_ExportLabels` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName, data__format` |
| `LabelingJobs_Get` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName` |
| `LabelingJobs_Pause` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName` |
| `LabelingJobs_Resume` | `EXEC` | `id, resourceGroupName, subscriptionId, workspaceName` |