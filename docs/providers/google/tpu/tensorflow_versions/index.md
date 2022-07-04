---
title: tensorflow_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - tensorflow_versions
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
<tr><td><b>Name</b></td><td><code>tensorflow_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.tpu.tensorflow_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name. |
| `version` | `string` | the tensorflow version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_tensorflowVersions_get` | `SELECT` | `name` | Gets TensorFlow Version. |
| `projects_locations_tensorflowVersions_list` | `SELECT` | `parent` | List TensorFlow versions supported by this API. |
