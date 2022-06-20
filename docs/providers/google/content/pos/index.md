---
title: pos
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.pos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#posListResponse`". |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, storeCode, targetMerchantId` | Retrieves information about the given store. |
| `list` | `SELECT` | `merchantId, targetMerchantId` | Lists the stores of the target merchant. |
| `insert` | `INSERT` | `merchantId, targetMerchantId` | Creates a store for the given merchant. |
| `delete` | `DELETE` | `merchantId, storeCode, targetMerchantId` | Deletes a store for the given merchant. |
| `custombatch` | `EXEC` |  | Batches multiple POS-related calls in a single request. |
| `inventory` | `EXEC` | `merchantId, targetMerchantId` | Submit inventory for the given merchant. |
| `sale` | `EXEC` | `merchantId, targetMerchantId` | Submit a sale event for the given merchant. |