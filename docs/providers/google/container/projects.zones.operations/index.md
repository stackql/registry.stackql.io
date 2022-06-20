---
title: projects.zones.operations
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
<tr><td><b>Name</b></td><td><code>projects.zones.operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.projects.zones.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `missingZones` | `array` | If any zones are listed here, the list of operations returned may be missing the operations from those zones. |
| `operations` | `array` | A list of operations in the project in the specified zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `operationId, projectId, zone` | Gets the specified operation. |
| `list` | `SELECT` | `projectId, zone` | Lists all operations in a project in a specific zone or all zones. |
| `cancel` | `EXEC` | `operationId, projectId, zone` | Cancels the specified operation. |
