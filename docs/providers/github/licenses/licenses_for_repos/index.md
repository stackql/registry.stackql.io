---
title: licenses_for_repos
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
<tr><td><b>Name</b></td><td><code>licenses_for_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.licenses.licenses_for_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` |  |
| `size` | `integer` |  |
| `sha` | `string` |  |
| `download_url` | `string` |  |
| `encoding` | `string` |  |
| `license` | `object` | License Simple |
| `url` | `string` |  |
| `_links` | `object` |  |
| `path` | `string` |  |
| `git_url` | `string` |  |
| `type` | `string` |  |
| `html_url` | `string` |  |
| `content` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get_for_repo` | `SELECT` | `owner, repo` |
