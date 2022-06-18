---
title: datafeeds
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
<tr><td><b>Name</b></td><td><code>datafeeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.datafeeds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#datafeedsListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of datafeeds. |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `datafeedId, merchantId` | Retrieves a datafeed configuration from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the configurations for datafeeds in your Merchant Center account. |
| `insert` | `INSERT` | `merchantId` | Registers a datafeed configuration with your Merchant Center account. |
| `delete` | `DELETE` | `datafeedId, merchantId` | Deletes a datafeed configuration from your Merchant Center account. |
| `custombatch` | `EXEC` |  | Deletes, fetches, gets, inserts and updates multiple datafeeds in a single request. |
| `fetchnow` | `EXEC` | `datafeedId, merchantId` | Invokes a fetch for the datafeed in your Merchant Center account. If you need to call this method more than once per day, we recommend you use the Products service to update your product data. |
| `update` | `EXEC` | `datafeedId, merchantId` | Updates a datafeed configuration of your Merchant Center account. Any fields that are not provided are deleted from the resource. |
