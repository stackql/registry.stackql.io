---
title: gists
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
<tr><td><b>Name</b></td><td><code>gists</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `created_at` | `string` |  |
| `files` | `object` |  |
| `url` | `string` |  |
| `truncated` | `boolean` |  |
| `updated_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `public` | `boolean` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | Simple User |
| `commits_url` | `string` |  |
| `fork_of` | `object` | Gist |
| `html_url` | `string` |  |
| `user` | `string` |  |
| `comments` | `integer` |  |
| `history` | `array` |  |
| `git_push_url` | `string` |  |
| `forks` | `array` |  |
| `forks_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `gist_id` |  |
| `get_revision` | `SELECT` | `gist_id, sha` |  |
| `list` | `SELECT` |  | Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists: |
| `list_for_user` | `SELECT` | `username` | Lists public gists for the specified user: |
| `create` | `INSERT` | `data__files` | Allows you to add a new gist with one or more files.<br /><br />**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally. |
| `delete` | `DELETE` | `gist_id` |  |
| `update` | `EXEC` | `gist_id` | Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged. |
