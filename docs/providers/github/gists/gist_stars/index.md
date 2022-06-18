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
<tr><td><b>Name</b></td><td><code>gist_stars</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_stars</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `git_push_url` | `string` |  |
| `forks_url` | `string` |  |
| `files` | `object` |  |
| `commits_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `user` | `object` | Simple User |
| `url` | `string` |  |
| `truncated` | `boolean` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `forks` | `array` |  |
| `history` | `array` |  |
| `owner` | `object` | Simple User |
| `updated_at` | `string` |  |
| `comments` | `integer` |  |
| `comments_url` | `string` |  |
| `public` | `boolean` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `check_is_starred` | `SELECT` | `gist_id` |  |
| `list_starred` | `SELECT` |  | List the authenticated user's starred gists: |
| `star` | `EXEC` | `gist_id` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar` | `EXEC` | `gist_id` |  |
