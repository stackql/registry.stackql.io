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
<tr><td><b>Name</b></td><td><code>github.repos.latest_releases</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.latest_releases</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `published_at` | `string` |  |
| `created_at` | `string` |  |
| `tarball_url` | `string` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `author` | `object` | Simple User |
| `discussion_url` | `string` | The URL of the release discussion. |
| `mentions_count` | `integer` |  |
| `body_html` | `string` |  |
| `url` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `assets_url` | `string` |  |
| `body` | `string` |  |
| `assets` | `array` |  |
| `body_text` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `zipball_url` | `string` |  |
| `reactions` | `object` |  |
| `upload_url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_latest_release` | `owner, repo` | View the latest published full release for the repository.<br /><br />The latest release is the most recent non-prerelease, non-draft release, sorted by the `created_at` attribute. The `created_at` attribute is the date of the commit used for the release, and not the date when the release was drafted or published. | SELECT |
