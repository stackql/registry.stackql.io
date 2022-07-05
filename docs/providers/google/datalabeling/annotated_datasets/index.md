---
title: annotated_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - annotated_datasets
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
<tr><td><b>Name</b></td><td><code>annotated_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.annotated_datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. AnnotatedDataset resource name in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id} |
| `description` | `string` | Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters. |
| `displayName` | `string` | Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters. |
| `exampleCount` | `string` | Output only. Number of examples in the annotated dataset. |
| `blockingResources` | `array` | Output only. The names of any related resources that are blocking changes to the annotated dataset. |
| `createTime` | `string` | Output only. Time the AnnotatedDataset was created. |
| `annotationType` | `string` | Output only. Type of the annotation. It is specified when starting labeling task. |
| `completedExampleCount` | `string` | Output only. Number of examples that have annotation in the annotated dataset. |
| `metadata` | `object` | Metadata on AnnotatedDataset. |
| `labelStats` | `object` | Statistics about annotation specs. |
| `annotationSource` | `string` | Output only. Source of the annotation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotatedDatasets_get` | `SELECT` | `name` | Gets an annotated dataset by resource name. |
| `projects_datasets_annotatedDatasets_list` | `SELECT` | `parent` | Lists annotated datasets for a dataset. Pagination is supported. |
| `projects_datasets_annotatedDatasets_delete` | `DELETE` | `name` | Deletes an annotated dataset by resource name. |
