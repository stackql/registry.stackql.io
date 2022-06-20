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
<tr><td><b>Id</b></td><td><code>google.blogger.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this resource. |
| `status` | `string` | The status of the comment (only populated for admin users). |
| `post` | `object` | Data about the post containing this comment. |
| `author` | `object` | The author of this Comment. |
| `kind` | `string` | The kind of this entry. Always blogger#comment. |
| `updated` | `string` | RFC 3339 date-time when this comment was last updated. |
| `content` | `string` | The actual content of the comment. May include HTML markup. |
| `blog` | `object` | Data about the blog containing this comment. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `inReplyTo` | `object` | Data about the comment this is in reply to. |
| `published` | `string` | RFC 3339 date-time when this comment was published. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blogId, commentId, postId` | Gets a comment by id. |
| `list` | `SELECT` | `blogId, postId` | Lists comments. |
| `delete` | `DELETE` | `blogId, commentId, postId` | Deletes a comment by blog id, post id and comment id. |
| `approve` | `EXEC` | `blogId, commentId, postId` | Marks a comment as not spam by blog id, post id and comment id. |
| `listByBlog` | `EXEC` | `blogId` | Lists comments by blog. |
| `markAsSpam` | `EXEC` | `blogId, commentId, postId` | Marks a comment as spam by blog id, post id and comment id. |
| `removeContent` | `EXEC` | `blogId, commentId, postId` | Removes the content of a comment by blog id, post id and comment id. |
