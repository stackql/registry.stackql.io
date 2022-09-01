---
title: workflow_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_versions
  - web_apps
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
<tr><td><b>Id</b></td><td><code>azure.web_apps.workflow_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `provisioningState` | `string` | The workflow provisioning state. |
| `version` | `string` | Gets the version. |
| `changedTime` | `string` | Gets the changed time. |
| `state` | `string` | The workflow state. |
| `tags` | `object` | The resource tags. |
| `location` | `string` | The resource location. |
| `accessControl` | `object` | The access control configuration. |
| `sku` | `object` | The sku type. |
| `createdTime` | `string` | Gets the created time. |
| `type` | `string` | Gets the resource type. |
| `parameters` | `object` | The parameters. |
| `accessEndpoint` | `string` | Gets the access endpoint. |
| `integrationAccount` | `object` | The resource reference. |
| `definition` | `object` |  |
| `endpointsConfiguration` | `object` | The endpoints configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowVersions_List` | `SELECT` | `name, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow versions. |
| `WorkflowVersions_Get` | `EXEC` | `name, resourceGroupName, subscriptionId, versionId, workflowName` | Gets a workflow version. |
