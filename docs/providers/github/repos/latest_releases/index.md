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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>latest_releases</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.latest_releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `tarball_url` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `zipball_url` | `string` |  |
| `html_url` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `author` | `object` | Simple User |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `mentions_count` | `integer` |  |
| `upload_url` | `string` |  |
| `assets` | `array` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `body_html` | `string` |  |
| `body` | `string` |  |
| `body_text` | `string` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `created_at` | `string` |  |
| `reactions` | `object` |  |
| `published_at` | `string` |  |
| `assets_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_latest_release` | `SELECT` | `owner, repo` |
