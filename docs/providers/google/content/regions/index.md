---
title: regions
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
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `regions` | `array` | The regions from the specified merchant. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `merchantId, regionId` | Retrieves a region defined in your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the regions in your Merchant Center account. |
| `create` | `INSERT` | `merchantId` | Creates a region definition in your Merchant Center account. |
| `delete` | `DELETE` | `merchantId, regionId` | Deletes a region definition from your Merchant Center account. |
| `patch` | `EXEC` | `merchantId, regionId` | Updates a region definition in your Merchant Center account. |
