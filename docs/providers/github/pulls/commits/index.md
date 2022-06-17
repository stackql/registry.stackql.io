---
title: commits
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
<tr><td><b>Name</b></td><td><code>github.pulls.commits</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.commits</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `commit` | `object` |  |
| `comments_url` | `string` |  |
| `html_url` | `string` |  |
| `parents` | `array` |  |
| `files` | `array` |  |
| `committer` | `object` | Simple User |
| `sha` | `string` |  |
| `stats` | `object` |  |
| `author` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_commits` | `owner, pull_number, repo` | Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://docs.github.com/rest/reference/repos#list-commits) endpoint. | SELECT |
