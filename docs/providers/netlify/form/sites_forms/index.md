---
title: sites_forms
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
<tr><td><b>Name</b></td><td><code>netlify.form.sites_forms</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.form.sites_forms</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `site_id` | `string` |  |
| `submission_count` | `integer` |  |
| `created_at` | `string` |  |
| `fields` | `array` |  |
| `paths` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `listSiteForms` | `site_id` |  | SELECT |
| `deleteSiteForm` | `form_id, site_id` |  | DELETE |