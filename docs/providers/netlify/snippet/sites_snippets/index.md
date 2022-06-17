---
title: sites_snippets
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
<tr><td><b>Name</b></td><td><code>netlify.snippet.sites_snippets</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.snippet.sites_snippets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `site_id` | `string` |  |
| `title` | `string` |  |
| `general` | `string` |  |
| `general_position` | `string` |  |
| `goal` | `string` |  |
| `goal_position` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSiteSnippet` | `site_id, snippet_id` |  | SELECT |
| `listSiteSnippets` | `site_id` |  | SELECT |
| `createSiteSnippet` | `site_id` |  | INSERT |
| `deleteSiteSnippet` | `site_id, snippet_id` |  | DELETE |
| `updateSiteSnippet` | `site_id, snippet_id` |  | EXEC |
