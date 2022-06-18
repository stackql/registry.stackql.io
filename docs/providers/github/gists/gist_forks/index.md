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
| `truncated` | `boolean` |  |
| `git_push_url` | `string` |  |
| `comments` | `integer` |  |
| `git_pull_url` | `string` |  |
| `comments_url` | `string` |  |
| `url` | `string` |  |
| `commits_url` | `string` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `history` | `array` |  |
| `files` | `object` |  |
| `forks` | `array` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `fork_of` | `object` | Gist |
| `owner` | `object` | Simple User |
| `public` | `boolean` |  |
| `user` | `string` |  |
| `forks_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list_forks` | `SELECT` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. |
