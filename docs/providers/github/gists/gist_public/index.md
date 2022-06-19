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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_public</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `public` | `boolean` |  |
| `comments` | `integer` |  |
| `owner` | `object` | Simple User |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `git_push_url` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `truncated` | `boolean` |  |
| `user` | `object` | Simple User |
| `forks` | `array` |  |
| `git_pull_url` | `string` |  |
| `comments_url` | `string` |  |
| `history` | `array` |  |
| `created_at` | `string` |  |
| `files` | `object` |  |
| `forks_url` | `string` |  |
| `commits_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
