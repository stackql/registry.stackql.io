---
title: recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_actions
  - maria_db
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
<tr><td><b>Name</b></td><td><code>recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.recommended_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `actionId` | `integer` | Recommendation action identifier. |
| `advisorName` | `string` | Advisor name. |
| `createdTime` | `string` | Recommendation action creation time. |
| `details` | `object` | Recommendation action details. |
| `expirationTime` | `string` | Recommendation action expiration time. |
| `reason` | `string` | Recommendation action reason. |
| `recommendationType` | `string` | Recommendation action type. |
| `sessionId` | `string` | Recommendation action session identifier. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RecommendedActions_ListByServer` | `SELECT` | `advisorName, resourceGroupName, serverName, subscriptionId` |
| `RecommendedActions_Get` | `EXEC` | `advisorName, recommendedActionName, resourceGroupName, serverName, subscriptionId` |
