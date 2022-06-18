---
title: users.threads
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
<tr><td><b>Name</b></td><td><code>users.threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gmail.users.threads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | Page token to retrieve the next page of results in the list. |
| `resultSizeEstimate` | `integer` | Estimated total number of results. |
| `threads` | `array` | List of threads. Note that each thread resource does not contain a list of `messages`. The list of `messages` for a given thread can be fetched using the threads.get method. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `id, userId` | Gets the specified thread. |
| `list` | `SELECT` | `userId` | Lists the threads in the user's mailbox. |
| `delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer `threads.trash` instead. |
| `modify` | `EXEC` | `id, userId` | Modifies the labels applied to the thread. This applies to all messages in the thread. |
| `trash` | `EXEC` | `id, userId` | Moves the specified thread to the trash. |
| `untrash` | `EXEC` | `id, userId` | Removes the specified thread from the trash. |
