---
title: workspace_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_settings
  - security
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
<tr><td><b>Name</b></td><td><code>workspace_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.workspace_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `scope` | `string` | All the VMs in this scope will send their security data to the mentioned workspace unless overridden by a setting with more specific scope |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `workspaceId` | `string` | The full Azure ID of the workspace to save the data in |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceSettings_List` | `SELECT` | `api-version, subscriptionId` | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| `WorkspaceSettings_Create` | `INSERT` | `api-version, subscriptionId, workspaceSettingName` | creating settings about where we should store your security data and logs |
| `WorkspaceSettings_Delete` | `DELETE` | `api-version, subscriptionId, workspaceSettingName` | Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace |
| `WorkspaceSettings_Get` | `EXEC` | `api-version, subscriptionId, workspaceSettingName` | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| `WorkspaceSettings_Update` | `EXEC` | `api-version, subscriptionId, workspaceSettingName` | Settings about where we should store your security data and logs |
