---
title: forms_submissions
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
<tr><td><b>Name</b></td><td><code>netlify.submission.forms_submissions</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.submission.forms_submissions</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `body` | `string` |  |
| `data` | `object` |  |
| `last_name` | `string` |  |
| `email` | `string` |  |
| `company` | `string` |  |
| `number` | `integer` |  |
| `site_url` | `string` |  |
| `summary` | `string` |  |
| `created_at` | `string` |  |
| `first_name` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `listFormSubmissions` | `form_id` |  | SELECT |
