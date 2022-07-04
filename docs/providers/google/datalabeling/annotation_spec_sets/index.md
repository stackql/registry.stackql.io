---
title: annotation_spec_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - annotation_spec_sets
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
<tr><td><b>Name</b></td><td><code>annotation_spec_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.annotation_spec_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The AnnotationSpecSet resource name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}" |
| `description` | `string` | Optional. User-provided description of the annotation specification set. The description can be up to 10,000 characters long. |
| `displayName` | `string` | Required. The display name for AnnotationSpecSet that you define when you create it. Maximum of 64 characters. |
| `annotationSpecs` | `array` | Required. The array of AnnotationSpecs that you define when you create the AnnotationSpecSet. These are the possible labels for the labeling task. |
| `blockingResources` | `array` | Output only. The names of any related resources that are blocking changes to the annotation spec set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_annotationSpecSets_get` | `SELECT` | `name` | Gets an annotation spec set by resource name. |
| `projects_annotationSpecSets_list` | `SELECT` | `parent` | Lists annotation spec sets for a project. Pagination is supported. |
| `projects_annotationSpecSets_create` | `INSERT` | `parent` | Creates an annotation spec set by providing a set of labels. |
| `projects_annotationSpecSets_delete` | `DELETE` | `name` | Deletes an annotation spec set by resource name. |