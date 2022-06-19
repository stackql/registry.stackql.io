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
<tr><td><b>Name</b></td><td><code>commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.commits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `text_matches` | `array` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `score` | `number` |  |
| `author` | `object` | Simple User |
| `commit` | `object` |  |
| `comments_url` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `parents` | `array` |  |
| `sha` | `string` |  |
| `committer` | `object` | Metaproperties for Git author/committer information. |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `commits` | `SELECT` | `q` |
