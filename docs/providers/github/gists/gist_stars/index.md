---
title: gist_stars
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
<tr><td><b>Name</b></td><td><code>github.gists.gist_stars</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_stars</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `created_at` | `string` |  |
| `git_push_url` | `string` |  |
| `files` | `object` |  |
| `updated_at` | `string` |  |
| `truncated` | `boolean` |  |
| `forks_url` | `string` |  |
| `forks` | `array` |  |
| `html_url` | `string` |  |
| `comments` | `integer` |  |
| `owner` | `object` | Simple User |
| `public` | `boolean` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `history` | `array` |  |
| `node_id` | `string` |  |
| `git_pull_url` | `string` |  |
| `url` | `string` |  |
| `user` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `check_is_starred` | `gist_id` |  | SELECT |
| `list_starred` | `` | List the authenticated user's starred gists: | SELECT |
| `star` | `gist_id` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." | EXEC |
| `unstar` | `gist_id` |  | EXEC |
