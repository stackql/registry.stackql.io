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
| `changedTime` | `string` | Gets the changed time. |
| `integrationAccount` | `object` | The resource reference. |
| `accessControl` | `object` | The access control configuration. |
| `createdTime` | `string` | Gets the created time. |
| `sku` | `object` | The sku type. |
| `type` | `string` | Gets the resource type. |
| `location` | `string` | The resource location. |
| `parameters` | `object` | The parameters. |
| `state` | `string` | The workflow state. |
| `accessEndpoint` | `string` | Gets the access endpoint. |
| `tags` | `object` | The resource tags. |
| `version` | `string` | Gets the version. |
| `endpointsConfiguration` | `object` | The endpoints configuration. |
| `provisioningState` | `string` | The workflow provisioning state. |
| `definition` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowVersions_List` | `SELECT` | `name, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow versions. |
| `WorkflowVersions_Get` | `EXEC` | `name, resourceGroupName, subscriptionId, versionId, workflowName` | Gets a workflow version. |
