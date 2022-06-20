---
title: products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token for the retrieval of the next page of products. |
| `resources` | `array` |  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#productsListResponse`". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, productId` | Retrieves a product from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the products in your Merchant Center account. The response might contain fewer items than specified by maxResults. Rely on nextPageToken to determine if there are more items to be requested. |
| `insert` | `INSERT` | `merchantId` | Uploads a product to your Merchant Center account. If an item with the same channel, contentLanguage, offerId, and targetCountry already exists, this method updates that entry. |
| `delete` | `DELETE` | `merchantId, productId` | Deletes a product from your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves, inserts, and deletes multiple products in a single request. |
| `update` | `EXEC` | `merchantId, productId` | Updates an existing product in your Merchant Center account. Only updates attributes provided in the request. |
