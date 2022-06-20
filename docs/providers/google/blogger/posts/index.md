---
title: posts
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
<tr><td><b>Name</b></td><td><code>posts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.blogger.posts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of this Post. |
| `content` | `string` | The content of the Post. May contain HTML markup. |
| `updated` | `string` | RFC 3339 date-time when this Post was last updated. |
| `replies` | `object` | The container of comments on this Post. |
| `labels` | `array` | The list of labels this Post was tagged with. |
| `etag` | `string` | Etag of the resource. |
| `published` | `string` | RFC 3339 date-time when this Post was published. |
| `customMetaData` | `string` | The JSON meta-data for the Post. |
| `title` | `string` | The title of the Post. |
| `location` | `object` | The location for geotagged posts. |
| `author` | `object` | The author of this Post. |
| `blog` | `object` | Data about the blog containing this Post. |
| `titleLink` | `string` | The title link URL, similar to atom's related link. |
| `images` | `array` | Display image for the Post. |
| `readerComments` | `string` | Comment control and display setting for readers of this post. |
| `url` | `string` | The URL where this Post is displayed. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `kind` | `string` | The kind of this entity. Always blogger#post. |
| `status` | `string` | Status of the post. Only set for admin-level requests. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blogId, postId` | Gets a post by blog id and post id |
| `list` | `SELECT` | `blogId` | Lists posts. |
| `insert` | `INSERT` | `blogId` | Inserts a post. |
| `delete` | `DELETE` | `blogId, postId` | Deletes a post by blog id and post id. |
| `getByPath` | `EXEC` | `blogId, path` | Gets a post by path. |
| `patch` | `EXEC` | `blogId, postId` | Patches a post. |
| `publish` | `EXEC` | `blogId, postId` | Publishes a post. |
| `revert` | `EXEC` | `blogId, postId` | Reverts a published or scheduled post to draft state. |
| `search` | `EXEC` | `blogId, q` | Searches for posts matching given query terms in the specified blog. |
| `update` | `EXEC` | `blogId, postId` | Updates a post by blog id and post id. |
