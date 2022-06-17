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
<tr><td><b>Name</b></td><td><code>github.gists.gists</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gists</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `forks` | `array` |  |
| `created_at` | `string` |  |
| `fork_of` | `object` | Gist |
| `owner` | `object` | Simple User |
| `forks_url` | `string` |  |
| `comments` | `integer` |  |
| `git_push_url` | `string` |  |
| `history` | `array` |  |
| `files` | `object` |  |
| `comments_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `public` | `boolean` |  |
| `truncated` | `boolean` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `commits_url` | `string` |  |
| `updated_at` | `string` |  |
| `user` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `gist_id` |  | SELECT |
| `get_revision` | `gist_id, sha` |  | SELECT |
| `list` | `` | Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists: | SELECT |
| `list_for_user` | `username` | Lists public gists for the specified user: | SELECT |
| `create` | `data__files` | Allows you to add a new gist with one or more files.<br /><br />**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally. | INSERT |
| `delete` | `gist_id` |  | DELETE |
| `update` | `gist_id` | Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged. | EXEC |
