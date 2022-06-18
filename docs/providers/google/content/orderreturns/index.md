---
title: orderreturns
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
<tr><td><b>Name</b></td><td><code>orderreturns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.orderreturns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#orderreturnsListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of returns. |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `merchantId, returnId` | Retrieves an order return from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists order returns in your Merchant Center account. |
| `acknowledge` | `EXEC` | `merchantId, returnId` | Acks an order return in your Merchant Center account. |
| `createorderreturn` | `EXEC` | `merchantId` | Create return in your Merchant Center account. |
| `process` | `EXEC` | `merchantId, returnId` | Processes return in your Merchant Center account. |
