---
title: sites_files
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
<tr><td><b>Name</b></td><td><code>sites_files</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.file.sites_files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `sha` | `string` |
| `size` | `integer` |
| `mime_type` | `string` |
| `path` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getSiteFileByPathName` | `SELECT` | `file_path, site_id` |
| `listSiteFiles` | `SELECT` | `site_id` |
