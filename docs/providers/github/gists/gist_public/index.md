---
title: gist_public
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
<tr><td><b>Name</b></td><td><code>gist_public</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_public</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `created_at` | `string` |  |
| `owner` | `object` | Simple User |
| `public` | `boolean` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `html_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `history` | `array` |  |
| `files` | `object` |  |
| `comments` | `integer` |  |
| `forks_url` | `string` |  |
| `user` | `object` | Simple User |
| `git_push_url` | `string` |  |
| `forks` | `array` |  |
| `commits_url` | `string` |  |
| `truncated` | `boolean` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
