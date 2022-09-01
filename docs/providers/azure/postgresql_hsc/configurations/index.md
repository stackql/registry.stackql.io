---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - postgresql_hsc
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
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Description of the configuration. |
| `defaultValue` | `string` | Default value of the configuration. |
| `source` | `string` | Source of the configuration. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `value` | `string` | Value of the configuration. |
| `allowedValues` | `string` | Allowed values of the configuration. |
| `dataType` | `string` | Data type of the configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Configurations_ListByServer` | `SELECT` | `resourceGroupName, serverGroupName, serverName, subscriptionId` | List all the configurations of a server in server group. |
| `Configurations_ListByServerGroup` | `SELECT` | `resourceGroupName, serverGroupName, subscriptionId` | List all the configurations of a server group. |
| `Configurations_Get` | `EXEC` | `configurationName, resourceGroupName, serverGroupName, subscriptionId` | Gets information about single server group configuration. |
| `Configurations_Update` | `EXEC` | `configurationName, resourceGroupName, serverGroupName, subscriptionId` | Updates configuration of server role groups in a server group |
