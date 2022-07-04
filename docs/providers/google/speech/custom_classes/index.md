---
title: custom_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_classes
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
<tr><td><b>Name</b></td><td><code>custom_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.speech.custom_classes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_customClasses_get` | `SELECT` | `name` | Get a custom class. |
| `projects_locations_customClasses_list` | `SELECT` | `parent` | List custom classes. |
| `projects_locations_customClasses_create` | `INSERT` | `parent` | Create a custom class. |
| `projects_locations_customClasses_delete` | `DELETE` | `name` | Delete a custom class. |
| `projects_locations_customClasses_patch` | `EXEC` | `name` | Update a custom class. |
