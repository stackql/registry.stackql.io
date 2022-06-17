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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github.repos.pages</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.pages</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `source` | `object` |  |
| `pending_domain_unverified_at` | `string` | The timestamp when a pending domain becomes unverified. |
| `protected_domain_state` | `string` | The state if the domain is verified |
| `cname` | `string` | The Pages site's custom domain |
| `html_url` | `string` | The web address the Page can be accessed from. |
| `custom_404` | `boolean` | Whether the Page has a custom 404 page. |
| `https_certificate` | `object` |  |
| `https_enforced` | `boolean` | Whether https is enabled on the domain |
| `public` | `boolean` | Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. |
| `status` | `string` | The status of the most recent build of the Page. |
| `url` | `string` | The API address for accessing this Page resource. |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_pages` | `owner, repo` |  | SELECT |
| `create_pages_site` | `owner, repo, data__source` | Configures a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages)." | INSERT |
| `delete_pages_site` | `owner, repo` |  | DELETE |
| `update_information_about_pages_site` | `owner, repo` | Updates information for a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages). | EXEC |
