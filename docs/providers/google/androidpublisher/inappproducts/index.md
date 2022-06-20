---
title: inappproducts
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
<tr><td><b>Name</b></td><td><code>inappproducts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidpublisher.inappproducts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `pageInfo` | `object` | Information about the current page. List operations that supports paging return only one "page" of results. This protocol buffer message describes the page that has been returned. |
| `tokenPagination` | `object` | Pagination information returned by a List operation when token pagination is enabled. List operations that supports paging return only one "page" of results. This protocol buffer message describes the page that has been returned. When using token pagination, clients should use the next/previous token to get another page of the result. The presence or absence of next/previous token indicates whether a next/previous page is available and provides a mean of accessing this page. ListRequest.page_token should be set to either next_page_token or previous_page_token to access another page. |
| `inappproduct` | `array` | All in-app products. |
| `kind` | `string` | The kind of this response ("androidpublisher#inappproductsListResponse"). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, sku` | Gets an in-app product, which can be a managed product or a subscription. |
| `list` | `SELECT` | `packageName` | Lists all in-app products - both managed products and subscriptions. If an app has a large number of in-app products, the response may be paginated. In this case the response field `tokenPagination.nextPageToken` will be set and the caller should provide its value as a `token` request parameter to retrieve the next page. |
| `insert` | `INSERT` | `packageName` | Creates an in-app product (i.e. a managed product or a subscriptions). |
| `delete` | `DELETE` | `packageName, sku` | Deletes an in-app product (i.e. a managed product or a subscriptions). |
| `patch` | `EXEC` | `packageName, sku` | Patches an in-app product (i.e. a managed product or a subscriptions). |
| `update` | `EXEC` | `packageName, sku` | Updates an in-app product (i.e. a managed product or a subscriptions). |
