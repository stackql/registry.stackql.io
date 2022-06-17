---
title: submissions
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
<tr><td><b>Name</b></td><td><code>netlify.submission.submissions</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.submission.submissions</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `company` | `string` |  |
| `data` | `object` |  |
| `email` | `string` |  |
| `number` | `integer` |  |
| `body` | `string` |  |
| `first_name` | `string` |  |
| `last_name` | `string` |  |
| `site_url` | `string` |  |
| `summary` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `listFormSubmission` | `submission_id` |  | SELECT |
| `deleteSubmission` | `submission_id` |  | DELETE |