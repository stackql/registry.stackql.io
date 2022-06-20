---
title: projects.locations.catalogs
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
<tr><td><b>Name</b></td><td><code>projects.locations.catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.projects.locations.catalogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `catalogs` | `array` | Output only. All the customer's catalogs. |
| `nextPageToken` | `string` | Pagination token, if not returned indicates the last page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the catalog configurations associated with the project. |
| `patch` | `EXEC` | `catalogsId, locationsId, projectsId` | Updates a catalog item. Partial updating is supported. Non-existing items will be created. |