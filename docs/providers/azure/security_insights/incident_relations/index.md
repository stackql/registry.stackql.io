---
title: incident_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_relations
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
<tr><td><b>Name</b></td><td><code>incident_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.incident_relations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `relatedResourceKind` | `string` | The resource kind of the related resource |
| `relatedResourceName` | `string` | The name of the related resource |
| `relatedResourceType` | `string` | The resource type of the related resource |
| `etag` | `string` | Etag of the azure resource |
| `relatedResourceId` | `string` | The resource ID of the related resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IncidentRelations_List` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident relations. |
| `IncidentRelations_CreateOrUpdate` | `INSERT` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the incident relation. |
| `IncidentRelations_Delete` | `DELETE` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Delete the incident relation. |
| `IncidentRelations_Get` | `EXEC` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Gets an incident relation. |
