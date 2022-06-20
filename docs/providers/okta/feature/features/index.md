---
title: features
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
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.feature.features</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `stage` | `object` |
| `status` | `string` |
| `type` | `string` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `featureId` |
| `list` | `SELECT` |  |
| `listFeatureDependencies` | `EXEC` | `featureId` |
| `listFeatureDependents` | `EXEC` | `featureId` |
| `updateFeatureLifecycle` | `EXEC` | `featureId, lifecycle` |