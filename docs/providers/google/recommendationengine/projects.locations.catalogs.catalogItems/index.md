---
title: projects.locations.catalogs.catalogItems
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
<tr><td><b>Name</b></td><td><code>projects.locations.catalogs.catalogItems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.projects.locations.catalogs.catalogItems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `catalogItems` | `array` | The catalog items. |
| `nextPageToken` | `string` | If empty, the list is complete. If nonempty, the token to pass to the next request's ListCatalogItemRequest.page_token. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `catalogItemsId, catalogsId, locationsId, projectsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `list` | `SELECT` | `catalogsId, locationsId, projectsId` | Gets a list of catalog items. |
| `create` | `INSERT` | `catalogsId, locationsId, projectsId` | Creates a catalog item. |
| `delete` | `DELETE` | `catalogItemsId, catalogsId, locationsId, projectsId` | Unregister an apiKey from using for predict method. |
| `import` | `EXEC` | `catalogsId, locationsId, projectsId` | Bulk import of multiple catalog items. Request processing may be synchronous. No partial updating supported. Non-existing items will be created. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully updated. |
| `patch` | `EXEC` | `catalogItemsId, catalogsId, locationsId, projectsId` | Updates a catalog item. Partial updating is supported. Non-existing items will be created. |
