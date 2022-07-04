---
title: authorized_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_domains
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
<tr><td><b>Name</b></td><td><code>authorized_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.authorized_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified domain name of the domain authorized for use. Example: example.com. |
| `name` | `string` | Full path to the AuthorizedDomain resource in the API. Example: apps/myapp/authorizedDomains/example.com.@OutputOnly |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `apps_authorizedDomains_list` | `SELECT` | `appsId` |
