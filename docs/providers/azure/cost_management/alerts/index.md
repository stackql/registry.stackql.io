---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - cost_management
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
<tr><td><b>Id</b></td><td><code>azure.cost_management.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `description` | `string` | Alert description |
| `details` | `object` | Alert details |
| `statusModificationUserName` | `string` | User who last modified the alert |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| `creationTime` | `string` | dateTime in which alert was created |
| `modificationTime` | `string` | dateTime in which alert was last modified |
| `costEntityId` | `string` | related budget |
| `type` | `string` | Resource type. |
| `statusModificationTime` | `string` | dateTime in which the alert status was last modified |
| `status` | `string` | alert status |
| `closeTime` | `string` | dateTime in which alert was closed |
| `definition` | `object` | defines the type of alert |
| `source` | `string` | Source of alert |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_List` | `SELECT` | `scope` | Lists the alerts for scope defined. |
| `Alerts_Dismiss` | `EXEC` | `alertId, scope` | Dismisses the specified alert |
| `Alerts_Get` | `EXEC` | `alertId, scope` | Gets the alert for the scope by alert ID. |
| `Alerts_ListExternal` | `EXEC` | `externalCloudProviderId, externalCloudProviderType` | Lists the Alerts for external cloud provider type defined. |