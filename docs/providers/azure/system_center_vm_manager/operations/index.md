---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - system_center_vm_manager
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
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name, in format of &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| `isDataAction` | `string` | Indicates whether the operation applies to data-plane. |
| `display` | `object` | Display metadata associated with the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
