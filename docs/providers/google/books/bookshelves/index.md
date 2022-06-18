---
title: bookshelves
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
<tr><td><b>Name</b></td><td><code>bookshelves</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.books.bookshelves</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Id of this bookshelf, only unique by user. |
| `description` | `string` | Description of this bookshelf. |
| `updated` | `string` | Last modified time of this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `kind` | `string` | Resource type for bookshelf metadata. |
| `volumesLastUpdated` | `string` | Last time a volume was added or removed from this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `selfLink` | `string` | URL to this resource. |
| `title` | `string` | Title of this bookshelf. |
| `volumeCount` | `integer` | Number of volumes in this bookshelf. |
| `access` | `string` | Whether this bookshelf is PUBLIC or PRIVATE. |
| `created` | `string` | Created time for this bookshelf (formatted UTC timestamp with millisecond resolution). |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `shelf, userId` | Retrieves metadata for a specific bookshelf for the specified user. |
| `list` | `SELECT` | `userId` | Retrieves a list of public bookshelves for the specified user. |
