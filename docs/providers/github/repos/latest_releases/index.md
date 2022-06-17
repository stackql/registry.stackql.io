---
title: latest_releases
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
<tr><td><b>Name</b></td><td><code>latest_releases</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.latest_releases</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `url` | `string` |  |
| `mentions_count` | `integer` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `assets_url` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `tag_name` | `string` | The name of the tag. |
| `assets` | `array` |  |
| `upload_url` | `string` |  |
| `zipball_url` | `string` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `tarball_url` | `string` |  |
| `body` | `string` |  |
| `author` | `object` | Simple User |
| `discussion_url` | `string` | The URL of the release discussion. |
| `body_text` | `string` |  |
| `reactions` | `object` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `published_at` | `string` |  |
| `node_id` | `string` |  |
| `body_html` | `string` |  |
## Methods
