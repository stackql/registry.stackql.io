---
title: workflow_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_versions
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>workflow_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `tags` | `object` | The resource tags. |
| `parameters` | `object` | The parameters. |
| `integrationAccount` | `object` | The resource reference. |
| `state` | `string` | The workflow state. |
| `sku` | `object` | The sku type. |
| `version` | `string` | Gets the version. |
| `location` | `string` | The resource location. |
| `accessControl` | `object` | The access control configuration. |
| `definition` | `object` |  |
| `type` | `string` | Gets the resource type. |
| `changedTime` | `string` | Gets the changed time. |
| `accessEndpoint` | `string` | Gets the access endpoint. |
| `createdTime` | `string` | Gets the created time. |
| `provisioningState` | `string` | The workflow provisioning state. |
| `endpointsConfiguration` | `object` | The endpoints configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowVersions_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow versions. |
| `WorkflowVersions_Get` | `EXEC` | `api-version, resourceGroupName, subscriptionId, versionId, workflowName` | Gets a workflow version. |
