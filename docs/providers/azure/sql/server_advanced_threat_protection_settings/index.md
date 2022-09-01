---
title: server_advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_advanced_threat_protection_settings
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
<tr><td><b>Name</b></td><td><code>server_advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_advanced_threat_protection_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationTime` | `string` | Specifies the UTC creation time of the policy. |
| `state` | `string` | Specifies the state of the Advanced Threat Protection, whether it is enabled or disabled or a state has not been applied yet on the specific database or server. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAdvancedThreatProtectionSettings_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Get a list of the server's Advanced Threat Protection states. |
| `ServerAdvancedThreatProtectionSettings_CreateOrUpdate` | `INSERT` | `advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId` | Creates or updates an Advanced Threat Protection state. |
| `ServerAdvancedThreatProtectionSettings_Get` | `EXEC` | `advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId` | Get a server's Advanced Threat Protection state. |
