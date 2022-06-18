---
title: comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#commentList". |
| `nextPageToken` | `string` | The page token for the next page of comments. This will be absent if the end of the comments list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
| `comments` | `array` | The list of comments. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `commentId, fileId` | Gets a comment by ID. |
| `list` | `SELECT` | `fileId` | Lists a file's comments. |
| `create` | `INSERT` | `fileId` | Creates a new comment on a file. |
| `delete` | `DELETE` | `commentId, fileId` | Deletes a comment. |
| `update` | `EXEC` | `commentId, fileId` | Updates a comment with patch semantics. |
