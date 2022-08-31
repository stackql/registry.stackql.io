---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - infrastructure_insights
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.infrastructure_insights.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `array` | Description of the alert. |
| `remediation` | `array` | Gets or sets the admin friendly remediation instructions for the alert. |
| `resourceRegistrationId` | `string` | Gets or sets the registration ID of the resource associated with the alert. If the alert is not associated with a resource, the resource registration ID is null. |
| `state` | `string` | State of the alert. |
| `faultTypeId` | `string` | Gets or sets the fault type ID of the alert. |
| `location` | `string` | The Azure Region where the resource lives |
| `resourceProviderRegistrationId` | `string` | Gets or sets the registration ID of the service the alert belongs to. |
| `impactedResourceDisplayName` | `string` | Display name for the impacted item. |
| `title` | `string` | Gets or sets the Resource ID for the impacted item. |
| `alertProperties` | `object` | Properties of the alert. |
| `faultId` | `string` | Gets or sets the fault ID of the alert. |
| `lastUpdatedTimestamp` | `string` | Timestamp when the alert was last updated. |
| `closedByUserAlias` | `string` | User alias who closed the alert. |
| `closedTimestamp` | `string` | Timestamp when the alert was closed. |
| `hasValidRemediationAction` | `boolean` | Indicates if the alert can be remediated. |
| `createdTimestamp` | `string` | Timestamp when the alert was created. |
| `severity` | `string` | Severity of the alert. |
| `alertId` | `string` | Gets or sets the ID of the alert. |
| `tags` | `object` | Resource tags. |
| `impactedResourceId` | `string` | Gets or sets the Resource ID for the impacted item. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_List` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns the list of all alerts in a given region. |
| `Alerts_Close` | `EXEC` | `alertName, location, resourceGroupName, subscriptionId, user` | Closes the given alert. |
| `Alerts_Get` | `EXEC` | `alertName, location, resourceGroupName, subscriptionId` | Returns the requested an alert. |
| `Alerts_Repair` | `EXEC` | `alertName, location, resourceGroupName, subscriptionId` | Repairs an alert. |
