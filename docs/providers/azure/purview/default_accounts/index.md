---
title: default_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_accounts
  - purview
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
<tr><td><b>Name</b></td><td><code>default_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.default_accounts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DefaultAccounts_Get` | `EXEC` | `api-version, scopeTenantId, scopeType` | Get the default account for the scope. |
| `DefaultAccounts_Remove` | `EXEC` | `api-version, scopeTenantId, scopeType` | Removes the default account from the scope. |
| `DefaultAccounts_Set` | `EXEC` | `api-version` | Sets the default account for the scope. |
