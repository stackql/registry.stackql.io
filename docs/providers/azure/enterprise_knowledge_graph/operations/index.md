---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - enterprise_knowledge_graph
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
<tr><td><b>Id</b></td><td><code>azure.enterprise_knowledge_graph.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: {provider}/{resource}/{operation}. |
| `origin` | `string` | The origin of the operation. |
| `properties` | `object` | Additional properties. |
| `display` | `object` | The operation supported by EnterpriseKnowledgeGraph Service Management. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |