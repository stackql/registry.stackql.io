---
title: replies
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
<tr><td><b>Name</b></td><td><code>replies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.drive.replies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#replyList". |
| `nextPageToken` | `string` | The page token for the next page of replies. This will be absent if the end of the replies list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |
| `replies` | `array` | The list of replies. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `commentId, fileId, replyId` | Gets a reply by ID. |
| `list` | `SELECT` | `commentId, fileId` | Lists a comment's replies. |
| `create` | `INSERT` | `commentId, fileId` | Creates a new reply to a comment. |
| `delete` | `DELETE` | `commentId, fileId, replyId` | Deletes a reply. |
| `update` | `EXEC` | `commentId, fileId, replyId` | Updates a reply with patch semantics. |
