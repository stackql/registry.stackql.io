---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - postgresql
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Description of the configuration. |
| `dataType` | `string` | Data type of the configuration. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `isReadOnly` | `boolean` | Configuration read-only or not. |
| `unit` | `string` | Configuration unit. |
| `defaultValue` | `string` | Default value of the configuration. |
| `isConfigPendingRestart` | `boolean` | Configuration is pending restart or not. |
| `allowedValues` | `string` | Allowed values of the configuration. |
| `value` | `string` | Value of the configuration. |
| `documentationLink` | `string` | Configuration documentation link. |
| `isDynamicConfig` | `boolean` | Configuration dynamic or static. |
| `source` | `string` | Source of the configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Configurations_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the configurations in a given server. |
| `Configurations_Get` | `EXEC` | `configurationName, resourceGroupName, serverName, subscriptionId` | Gets information about a configuration of server. |
| `Configurations_Put` | `EXEC` | `configurationName, resourceGroupName, serverName, subscriptionId` | Updates a configuration of a server. |
| `Configurations_Update` | `EXEC` | `configurationName, resourceGroupName, serverName, subscriptionId` | Updates a configuration of a server. |
