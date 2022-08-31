---
title: adc_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - adc_operations
  - data_catalog
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
<tr><td><b>Name</b></td><td><code>adc_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_catalog.adc_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: {provider}/{resource}/{operation}. |
| `display` | `object` | The operation supported by Azure Data Catalog Service. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ADCOperations_List` | `SELECT` |  |