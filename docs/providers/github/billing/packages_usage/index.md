---
title: packages_usage
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
<tr><td><b>Name</b></td><td><code>packages_usage</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.packages_usage</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `included_gigabytes_bandwidth` | `integer` | Free storage space (GB) for GitHub Packages. |
| `total_gigabytes_bandwidth_used` | `integer` | Sum of the free and paid storage space (GB) for GitHuub Packages. |
| `total_paid_gigabytes_bandwidth_used` | `integer` | Total paid storage space (GB) for GitHuub Packages. |
## Methods
