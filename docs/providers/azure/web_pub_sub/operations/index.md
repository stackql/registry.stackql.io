---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - web_pub_sub
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
<tr><td><b>Id</b></td><td><code>azure.web_pub_sub.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the operation with format: {provider}/{resource}/{operation} |
| `origin` | `string` | Optional. The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. |
| `properties` | `object` | Extra Operation properties. |
| `display` | `object` | The object that describes a operation. |
| `isDataAction` | `boolean` | If the operation is a data action. (for data plane rbac) |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |