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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.latest_releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `upload_url` | `string` |  |
| `assets` | `array` |  |
| `mentions_count` | `integer` |  |
| `node_id` | `string` |  |
| `body_html` | `string` |  |
| `author` | `object` | Simple User |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `discussion_url` | `string` | The URL of the release discussion. |
| `tarball_url` | `string` |  |
| `html_url` | `string` |  |
| `zipball_url` | `string` |  |
| `url` | `string` |  |
| `assets_url` | `string` |  |
| `reactions` | `object` |  |
| `created_at` | `string` |  |
| `body` | `string` |  |
| `published_at` | `string` |  |
| `body_text` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_latest_release` | `SELECT` | `owner, repo` |
