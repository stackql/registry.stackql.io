---
title: shared_storage
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
<tr><td><b>Name</b></td><td><code>shared_storage</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.shared_storage</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `days_left_in_billing_cycle` | `integer` | Numbers of days left in billing cycle. |
| `estimated_paid_storage_for_month` | `integer` | Estimated storage space (GB) used in billing cycle. |
| `estimated_storage_for_month` | `integer` | Estimated sum of free and paid storage space (GB) used in billing cycle. |
## Methods
