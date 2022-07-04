---
title: data_items
hide_title: false
hide_table_of_contents: false
keywords:
  - data_items
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
<tr><td><b>Name</b></td><td><code>data_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.data_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the data item, in format of: projects/{project_id}/datasets/{dataset_id}/dataItems/{data_item_id} |
| `videoPayload` | `object` | Container of information of a video. |
| `imagePayload` | `object` | Container of information about an image. |
| `textPayload` | `object` | Container of information about a piece of text. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotatedDatasets_dataItems_get` | `SELECT` | `name` | Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset. |
| `projects_datasets_annotatedDatasets_dataItems_list` | `SELECT` | `parent` | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
| `projects_datasets_dataItems_get` | `SELECT` | `name` | Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset. |
| `projects_datasets_dataItems_list` | `SELECT` | `parent` | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
