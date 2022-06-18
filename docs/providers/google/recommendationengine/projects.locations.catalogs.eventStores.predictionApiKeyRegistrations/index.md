---
title: projects.locations.catalogs.eventStores.predictionApiKeyRegistrations
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
<tr><td><b>Name</b></td><td><code>projects.locations.catalogs.eventStores.predictionApiKeyRegistrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.projects.locations.catalogs.eventStores.predictionApiKeyRegistrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `predictionApiKeyRegistrations` | `array` | The list of registered API keys. |
| `nextPageToken` | `string` | If empty, the list is complete. If nonempty, pass the token to the next request's `ListPredictionApiKeysRegistrationsRequest.pageToken`. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `catalogsId, eventStoresId, locationsId, projectsId` | List the registered apiKeys for use with predict method. |
| `create` | `INSERT` | `catalogsId, eventStoresId, locationsId, projectsId` | Register an API key for use with predict method. |
| `delete` | `DELETE` | `catalogsId, eventStoresId, locationsId, predictionApiKeyRegistrationsId, projectsId` | Unregister an apiKey from using for predict method. |
