---
title: accounts.creatives
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
<tr><td><b>Name</b></td><td><code>accounts.creatives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adexchangebuyer2.accounts.creatives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `creatives` | `array` | The list of creatives. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListCreativesRequest.page_token field in the subsequent call to `ListCreatives` method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId, creativeId` | Gets a creative. |
| `list` | `SELECT` | `accountId` | Lists creatives. |
| `create` | `INSERT` | `accountId` | Creates a creative. |
| `stopWatching` | `EXEC` | `accountId, creativeId` | Stops watching a creative. Will stop push notifications being sent to the topics when the creative changes status. |
| `update` | `EXEC` | `accountId, creativeId` | Updates a creative. |
| `watch` | `EXEC` | `accountId, creativeId` | Watches a creative. Will result in push notifications being sent to the topic when the creative changes status. |
