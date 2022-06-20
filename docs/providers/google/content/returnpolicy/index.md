---
title: returnpolicy
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
<tr><td><b>Name</b></td><td><code>returnpolicy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.returnpolicy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#returnpolicyListResponse`". |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, returnPolicyId` | Gets a return policy of the Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the return policies of the Merchant Center account. |
| `insert` | `INSERT` | `merchantId` | Inserts a return policy for the Merchant Center account. |
| `delete` | `DELETE` | `merchantId, returnPolicyId` | Deletes a return policy for the given Merchant Center account. |
| `custombatch` | `EXEC` |  | Batches multiple return policy related calls in a single request. |
