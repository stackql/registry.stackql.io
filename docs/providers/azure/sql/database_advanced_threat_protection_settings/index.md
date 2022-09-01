---
title: database_advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - database_advanced_threat_protection_settings
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
<tr><td><b>Name</b></td><td><code>database_advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_advanced_threat_protection_settings</code></td></tr>
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
| `DatabaseAdvancedThreatProtectionSettings_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of database's Advanced Threat Protection states. |
| `DatabaseAdvancedThreatProtectionSettings_CreateOrUpdate` | `INSERT` | `advancedThreatProtectionName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates a database's Advanced Threat Protection state. |
| `DatabaseAdvancedThreatProtectionSettings_Get` | `EXEC` | `advancedThreatProtectionName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database's Advanced Threat Protection state. |
