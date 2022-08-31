---
title: time_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - time_zones
  - sql
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
<tr><td><b>Name</b></td><td><code>time_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.time_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `displayName` | `string` | The time zone display name |
| `timeZoneId` | `string` | The time zone id |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TimeZones_ListByLocation` | `SELECT` | `locationName, subscriptionId` | Gets a list of managed instance time zones by location. |
| `TimeZones_Get` | `EXEC` | `locationName, subscriptionId, timeZoneId` | Gets a managed instance time zone. |
