---
title: advanced_threat_protection
hide_title: false
hide_table_of_contents: false
keywords:
  - advanced_threat_protection
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
<tr><td><b>Name</b></td><td><code>advanced_threat_protection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.advanced_threat_protection</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AdvancedThreatProtection_Create` | `INSERT` | `api-version, resourceId, settingName` | Creates or updates the Advanced Threat Protection settings on a specified resource. |
| `AdvancedThreatProtection_Get` | `EXEC` | `api-version, resourceId, settingName` | Gets the Advanced Threat Protection settings for the specified resource. |
