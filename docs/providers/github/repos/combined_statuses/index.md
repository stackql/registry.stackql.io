---
title: combined_statuses
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
<tr><td><b>Name</b></td><td><code>github.repos.combined_statuses</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.combined_statuses</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `commit_url` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `sha` | `string` |  |
| `state` | `string` |  |
| `statuses` | `array` |  |
| `total_count` | `integer` |  |
| `url` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_combined_status_for_ref` | `owner, ref, repo` | Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.<br /><br /><br />Additionally, a combined `state` is returned. The `state` is one of:<br /><br />*   **failure** if any of the contexts report as `error` or `failure`<br />*   **pending** if there are no statuses or a context is `pending`<br />*   **success** if the latest status for all contexts is `success` | SELECT |
