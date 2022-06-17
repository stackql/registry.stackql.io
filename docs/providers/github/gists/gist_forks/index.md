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
<tr><td><b>Name</b></td><td><code>github.gists.gist_forks</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_forks</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `history` | `array` |  |
| `comments_url` | `string` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `git_pull_url` | `string` |  |
| `truncated` | `boolean` |  |
| `user` | `string` |  |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `fork_of` | `object` | Gist |
| `files` | `object` |  |
| `git_push_url` | `string` |  |
| `created_at` | `string` |  |
| `owner` | `object` | Simple User |
| `comments` | `integer` |  |
| `forks` | `array` |  |
| `public` | `boolean` |  |
| `commits_url` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_forks` | `gist_id` |  | SELECT |
| `fork` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. | EXEC |
