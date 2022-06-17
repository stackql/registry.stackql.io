---
title: actions_usage
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
<tr><td><b>Name</b></td><td><code>actions_usage</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.actions_usage</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `total_minutes_used` | `integer` | The sum of the free and paid GitHub Actions minutes used. |
| `total_paid_minutes_used` | `integer` | The total paid GitHub Actions minutes used. |
| `included_minutes` | `integer` | The amount of free GitHub Actions minutes available. |
| `minutes_used_breakdown` | `object` |  |
## Methods
