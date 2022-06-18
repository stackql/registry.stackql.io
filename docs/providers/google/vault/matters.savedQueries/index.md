---
title: matters.savedQueries
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
<tr><td><b>Name</b></td><td><code>matters.savedQueries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vault.matters.savedQueries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | Page token to retrieve the next page of results in the list. If this is empty, then there are no more saved queries to list. |
| `savedQueries` | `array` | List of saved queries. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `matterId, savedQueryId` | Retrieves the specified saved query. |
| `list` | `SELECT` | `matterId` | Lists the saved queries in a matter. |
| `create` | `INSERT` | `matterId` | Creates a saved query. |
| `delete` | `DELETE` | `matterId, savedQueryId` | Deletes the specified saved query. |
