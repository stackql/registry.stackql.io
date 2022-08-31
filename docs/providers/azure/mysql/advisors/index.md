---
title: advisors
hide_title: false
hide_table_of_contents: false
keywords:
  - advisors
  - mysql
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
<tr><td><b>Name</b></td><td><code>advisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.advisors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Link to retrieve next page of results. |
| `value` | `array` | The list of recommendation action advisors. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Advisors_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List recommendation action advisors. |
| `Advisors_Get` | `EXEC` | `advisorName, resourceGroupName, serverName, subscriptionId` | Get a recommendation action advisor. |
