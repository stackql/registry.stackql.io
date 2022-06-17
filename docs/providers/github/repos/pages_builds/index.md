---
title: pages_builds
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
<tr><td><b>Name</b></td><td><code>github.repos.pages_builds</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.pages_builds</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `error` | `object` |  |
| `pusher` | `object` | Simple User |
| `status` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `commit` | `string` |  |
| `created_at` | `string` |  |
| `duration` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_pages_build` | `build_id, owner, repo` |  | SELECT |
| `list_pages_builds` | `owner, repo` |  | SELECT |
| `request_pages_build` | `owner, repo` | You can request that your site be built from the latest revision on the default branch. This has the same effect as pushing a commit to your default branch, but does not require an additional commit. Manually triggering page builds can be helpful when diagnosing build warnings and failures.<br /><br />Build requests are limited to one concurrent build per repository and one concurrent build per requester. If you request a build while another is still in progress, the second request will be queued until the first completes. | EXEC |
