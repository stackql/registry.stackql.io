---
title: gist_forks
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
<tr><td><b>Name</b></td><td><code>gist_forks</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_forks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | Simple User |
| `git_pull_url` | `string` |  |
| `history` | `array` |  |
| `updated_at` | `string` |  |
| `fork_of` | `object` | Gist |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `user` | `string` |  |
| `forks_url` | `string` |  |
| `public` | `boolean` |  |
| `truncated` | `boolean` |  |
| `forks` | `array` |  |
| `files` | `object` |  |
| `comments` | `integer` |  |
| `node_id` | `string` |  |
| `commits_url` | `string` |  |
| `git_push_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_forks` | `SELECT` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. |
