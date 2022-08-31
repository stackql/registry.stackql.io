---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - security_insights
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
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.source_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id (a Guid) of the source control |
| `description` | `string` | A description of the source control |
| `lastDeploymentInfo` | `object` | Information regarding a deployment. |
| `contentTypes` | `array` | Array of source control content types. |
| `displayName` | `string` | The display name of the source control |
| `repoType` | `string` | The type of repository. |
| `version` | `string` | The version of the source control. |
| `repository` | `object` | metadata of a repository. |
| `etag` | `string` | Etag of the azure resource |
| `repositoryResourceInfo` | `object` | Resources created in user's repository for the source-control. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SourceControls_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all source controls, without source control items. |
| `SourceControls_Create` | `INSERT` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Creates a source control. |
| `SourceControls_Delete` | `DELETE` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Delete a source control. |
| `SourceControls_Get` | `EXEC` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Gets a source control byt its identifier. |
