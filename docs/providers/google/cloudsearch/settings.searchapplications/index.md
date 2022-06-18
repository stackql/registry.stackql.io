---
title: settings.searchapplications
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
<tr><td><b>Name</b></td><td><code>settings.searchapplications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.settings.searchapplications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `searchApplications` | `array` |  |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `searchapplicationsId` | Gets the specified search application. **Note:** This API requires an admin account to execute. |
| `list` | `SELECT` |  | Lists all search applications. **Note:** This API requires an admin account to execute. |
| `create` | `INSERT` |  | Creates a search application. **Note:** This API requires an admin account to execute. |
| `delete` | `DELETE` | `searchapplicationsId` | Deletes a search application. **Note:** This API requires an admin account to execute. |
| `reset` | `EXEC` | `searchapplicationsId` | Resets a search application to default settings. This will return an empty response. **Note:** This API requires an admin account to execute. |
| `update` | `EXEC` | `searchapplicationsId` | Updates a search application. **Note:** This API requires an admin account to execute. |
