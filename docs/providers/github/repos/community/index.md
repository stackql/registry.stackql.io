---
title: community
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
<tr><td><b>Name</b></td><td><code>github.repos.community</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.community</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `description` | `string` |  |
| `documentation` | `string` |  |
| `files` | `object` |  |
| `health_percentage` | `integer` |  |
| `updated_at` | `string` |  |
| `content_reports_enabled` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_community_profile_metrics` | `owner, repo` | This endpoint will return all community profile metrics, including an<br />overall health score, repository description, the presence of documentation, detected<br />code of conduct, detected license, and the presence of ISSUE\_TEMPLATE, PULL\_REQUEST\_TEMPLATE,<br />README, and CONTRIBUTING files.<br /><br />The `health_percentage` score is defined as a percentage of how many of<br />these four documents are present: README, CONTRIBUTING, LICENSE, and<br />CODE_OF_CONDUCT. For example, if all four documents are present, then<br />the `health_percentage` is `100`. If only one is present, then the<br />`health_percentage` is `25`.<br /><br />`content_reports_enabled` is only returned for organization-owned repositories. | SELECT |
