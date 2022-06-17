---
title: pages
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.pages</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `https_certificate` | `object` |  |
| `url` | `string` | The API address for accessing this Page resource. |
| `pending_domain_unverified_at` | `string` | The timestamp when a pending domain becomes unverified. |
| `protected_domain_state` | `string` | The state if the domain is verified |
| `custom_404` | `boolean` | Whether the Page has a custom 404 page. |
| `status` | `string` | The status of the most recent build of the Page. |
| `public` | `boolean` | Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. |
| `https_enforced` | `boolean` | Whether https is enabled on the domain |
| `cname` | `string` | The Pages site's custom domain |
| `source` | `object` |  |
| `html_url` | `string` | The web address the Page can be accessed from. |
## Methods
