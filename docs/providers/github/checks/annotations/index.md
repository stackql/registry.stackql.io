---
title: annotations
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
<tr><td><b>Name</b></td><td><code>github.checks.annotations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.checks.annotations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `raw_details` | `string` |  |
| `blob_href` | `string` |  |
| `title` | `string` |  |
| `end_column` | `integer` |  |
| `annotation_level` | `string` |  |
| `start_line` | `integer` |  |
| `path` | `string` |  |
| `start_column` | `integer` |  |
| `end_line` | `integer` |  |
| `message` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_annotations` | `check_run_id, owner, repo` | Lists annotations for a check run using the annotation `id`. GitHub Apps must have the `checks:read` permission on a private repository or pull access to a public repository to get annotations for a check run. OAuth Apps and authenticated users must have the `repo` scope to get annotations for a check run in a private repository. | SELECT |
