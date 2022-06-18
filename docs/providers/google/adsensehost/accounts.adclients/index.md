---
title: accounts.adclients
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
<tr><td><b>Name</b></td><td><code>accounts.adclients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adsensehost.accounts.adclients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Unique identifier of this ad client. |
| `arcOptIn` | `boolean` | Whether this ad client is opted in to ARC. |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#adClient. |
| `productCode` | `string` | This ad client's product code, which corresponds to the PRODUCT_CODE report dimension. |
| `supportsReporting` | `boolean` | Whether this ad client supports being reported on. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, adClientId` | Get information about one of the ad clients in the specified publisher's AdSense account. |
| `list` | `SELECT` | `accountId` | List all hosted ad clients in the specified hosted account. |
