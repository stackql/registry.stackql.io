---
title: pages
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
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.blogger.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | The identifier for this resource. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `content` | `string` | The body content of this Page, in HTML. |
| `published` | `string` | RFC 3339 date-time when this Page was published. |
| `author` | `object` | The author of this Page. |
| `blog` | `object` | Data about the blog containing this Page. |
| `updated` | `string` | RFC 3339 date-time when this Page was last updated. |
| `url` | `string` | The URL that this Page is displayed at. |
| `kind` | `string` | The kind of this entity. Always blogger#page. |
| `etag` | `string` | Etag of the resource. |
| `title` | `string` | The title of this entity. This is the name displayed in the Admin user interface. |
| `status` | `string` | The status of the page for admin resources (either LIVE or DRAFT). |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `blogId, pageId` | Gets a page by blog id and page id. |
| `list` | `SELECT` | `blogId` | Lists pages. |
| `insert` | `INSERT` | `blogId` | Inserts a page. |
| `delete` | `DELETE` | `blogId, pageId` | Deletes a page by blog id and page id. |
| `patch` | `EXEC` | `blogId, pageId` | Patches a page. |
| `publish` | `EXEC` | `blogId, pageId` | Publishes a page. |
| `revert` | `EXEC` | `blogId, pageId` | Reverts a published or scheduled page to draft state. |
| `update` | `EXEC` | `blogId, pageId` | Updates a page by blog id and page id. |
