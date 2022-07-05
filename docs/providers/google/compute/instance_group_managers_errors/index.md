---
title: instance_group_managers_errors
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers_errors
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
<tr><td><b>Name</b></td><td><code>instance_group_managers_errors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_group_managers_errors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceActionDetails` | `object` |  |
| `timestamp` | `string` | [Output Only] The time that this error occurred. This value is in RFC3339 text format. |
| `error` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instanceGroupManagers_listErrors` | `SELECT` | `instanceGroupManager, project, zone` |
