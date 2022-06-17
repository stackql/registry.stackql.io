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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commits</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commits</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `commit` | `object` |  |
| `html_url` | `string` |  |
| `stats` | `object` |  |
| `parents` | `array` |  |
| `sha` | `string` |  |
| `committer` | `object` | Simple User |
| `author` | `object` | Simple User |
| `files` | `array` |  |
| `comments_url` | `string` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
## Methods
