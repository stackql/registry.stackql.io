---
title: models
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
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `models` | `array` | Models in the requested dataset. Only the following fields are populated: model_reference, model_type, creation_time, last_modified_time and labels. |
| `nextPageToken` | `string` | A token to request the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetsId, modelsId, projectsId` | Gets the specified model resource by model ID. |
| `list` | `SELECT` | `datasetsId, projectsId` | Lists all models in the specified dataset. Requires the READER dataset role. After retrieving the list of models, you can get information about a particular model by calling the models.get method. |
| `delete` | `DELETE` | `datasetsId, modelsId, projectsId` | Deletes the model specified by modelId from the dataset. |
| `patch` | `EXEC` | `datasetsId, modelsId, projectsId` | Patch specific fields in the specified model. |
