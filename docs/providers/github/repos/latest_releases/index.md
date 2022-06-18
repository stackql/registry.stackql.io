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
| `created_at` | `string` |  |
| `tarball_url` | `string` |  |
| `author` | `object` | Simple User |
| `body_text` | `string` |  |
| `published_at` | `string` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `reactions` | `object` |  |
| `upload_url` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `assets` | `array` |  |
| `zipball_url` | `string` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `body_html` | `string` |  |
| `url` | `string` |  |
| `body` | `string` |  |
| `assets_url` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `mentions_count` | `integer` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `tag_name` | `string` | The name of the tag. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_latest_release` | `SELECT` | `owner, repo` |
