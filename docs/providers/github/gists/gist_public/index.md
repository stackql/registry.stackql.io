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
| `owner` | `object` | Simple User |
| `comments` | `integer` |  |
| `truncated` | `boolean` |  |
| `history` | `array` |  |
| `commits_url` | `string` |  |
| `user` | `object` | Simple User |
| `public` | `boolean` |  |
| `forks` | `array` |  |
| `comments_url` | `string` |  |
| `html_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `files` | `object` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `forks_url` | `string` |  |
| `git_push_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_public` | `SELECT` |  |
