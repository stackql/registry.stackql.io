---
title: releases
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
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.releases</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `published_at` | `string` |  |
| `body` | `string` |  |
| `node_id` | `string` |  |
| `assets` | `array` |  |
| `created_at` | `string` |  |
| `tarball_url` | `string` |  |
| `upload_url` | `string` |  |
| `html_url` | `string` |  |
| `assets_url` | `string` |  |
| `mentions_count` | `integer` |  |
| `url` | `string` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `zipball_url` | `string` |  |
| `body_html` | `string` |  |
| `body_text` | `string` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `reactions` | `object` |  |
| `author` | `object` | Simple User |
## Methods
