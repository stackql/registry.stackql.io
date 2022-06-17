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
<tr><td><b>Name</b></td><td><code>github.gists.gist_public</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_public</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `files` | `object` |  |
| `updated_at` | `string` |  |
| `user` | `object` | Simple User |
| `history` | `array` |  |
| `comments` | `integer` |  |
| `html_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `forks_url` | `string` |  |
| `truncated` | `boolean` |  |
| `forks` | `array` |  |
| `created_at` | `string` |  |
| `comments_url` | `string` |  |
| `public` | `boolean` |  |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `owner` | `object` | Simple User |
| `commits_url` | `string` |  |
| `git_push_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_public` | `` | List public gists sorted by most recently updated to least recently updated.<br /><br />Note: With [pagination](https://docs.github.com/rest/overview/resources-in-the-rest-api#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page. | SELECT |
