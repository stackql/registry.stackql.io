---
title: changes
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
<tr><td><b>Name</b></td><td><code>changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.changes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#changeList". |
| `newStartPageToken` | `string` | The starting page token for future changes. This will be present only if the end of the current changes list has been reached. |
| `nextPageToken` | `string` | The page token for the next page of changes. This will be absent if the end of the changes list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
| `changes` | `array` | The list of changes. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `pageToken` | Lists the changes for a user or shared drive. |
| `getStartPageToken` | `EXEC` |  | Gets the starting pageToken for listing future changes. |
| `watch` | `EXEC` | `pageToken` | Subscribes to changes for a user. |
