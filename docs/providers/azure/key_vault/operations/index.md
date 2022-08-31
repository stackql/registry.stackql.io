---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - key_vault
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: {provider}/{resource}/{operation} |
| `origin` | `string` | The origin of operations. |
| `serviceSpecification` | `object` | One property of operation, include log specifications. |
| `display` | `` | Display metadata associated with the operation. |
| `isDataAction` | `boolean` | Property to specify whether the action is a data action. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
