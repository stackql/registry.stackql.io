---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the incident |
| `additionalData` | `object` | Incident additional data property bag. |
| `providerIncidentId` | `string` | The incident ID assigned by the incident provider |
| `etag` | `string` | Etag of the azure resource |
| `incidentUrl` | `string` | The deep-link url to the incident in Azure portal |
| `classification` | `string` | The reason the incident was closed |
| `firstActivityTimeUtc` | `string` | The time of the first activity in the incident |
| `createdTimeUtc` | `string` | The time the incident was created |
| `teamInformation` | `object` | Describes team information |
| `lastActivityTimeUtc` | `string` | The time of the last activity in the incident |
| `severity` | `string` | The severity of the incident |
| `classificationReason` | `string` | The classification reason the incident was closed with |
| `status` | `string` | The status of the incident |
| `incidentNumber` | `integer` | A sequential number |
| `providerName` | `string` | The name of the source provider that generated the incident |
| `title` | `string` | The title of the incident |
| `classificationComment` | `string` | Describes the reason the incident was closed |
| `relatedAnalyticRuleIds` | `array` | List of resource ids of Analytic rules related to the incident |
| `owner` | `object` | Information on the user an incident is assigned to |
| `lastModifiedTimeUtc` | `string` | The last time the incident was updated |
| `labels` | `array` | List of labels relevant to this incident |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Incidents_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all incidents. |
| `Incidents_CreateOrUpdate` | `INSERT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the incident. |
| `Incidents_Delete` | `DELETE` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Delete the incident. |
| `Incidents_CreateTeam` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName, data__teamName` | Creates a Microsoft team to investigate the incident by sharing information and insights between participants. |
| `Incidents_Get` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets an incident. |
| `Incidents_ListAlerts` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident alerts. |
| `Incidents_ListBookmarks` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident bookmarks. |
| `Incidents_ListEntities` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident related entities. |
| `Incidents_RunPlaybook` | `EXEC` | `incidentIdentifier, resourceGroupName, subscriptionId, workspaceName` | Triggers playbook on a specific incident |
