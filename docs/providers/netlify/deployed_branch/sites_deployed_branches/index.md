---
title: sites_deployed_branches
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
<tr><td><b>Name</b></td><td><code>netlify.deployed_branch.sites_deployed_branches</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deployed_branch.sites_deployed_branches</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `ssl_url` | `string` |  |
| `url` | `string` |  |
| `deploy_id` | `string` |  |
| `slug` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `listSiteDeployedBranches` | `site_id` |  | SELECT |
