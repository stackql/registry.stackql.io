---
title: blogs
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
<tr><td><b>Name</b></td><td><code>blogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.blogger.blogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this resource. |
| `name` | `string` | The name of this blog. This is displayed as the title. |
| `description` | `string` | The description of this blog. This is displayed underneath the title. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `updated` | `string` | RFC 3339 date-time when this blog was last updated. |
| `customMetaData` | `string` | The JSON custom meta-data for the Blog. |
| `locale` | `object` | The locale this Blog is set to. |
| `posts` | `object` | The container of posts in this blog. |
| `published` | `string` | RFC 3339 date-time when this blog was published. |
| `url` | `string` | The URL where this blog is published. |
| `pages` | `object` | The container of pages in this blog. |
| `kind` | `string` | The kind of this entry. Always blogger#blog. |
| `status` | `string` | The status of the blog. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blogId` | Gets a blog by id. |
| `getByUrl` | `EXEC` | `url` | Gets a blog by url. |
| `listByUser` | `EXEC` | `userId` | Lists blogs by user. |
