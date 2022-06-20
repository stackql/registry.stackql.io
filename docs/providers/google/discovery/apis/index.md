---
title: apis
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.discovery.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of this API. |
| `name` | `string` | The name of the API. |
| `description` | `string` | The description of this API. |
| `preferred` | `boolean` | True if this version is the preferred version to use. |
| `labels` | `array` | Labels for the status of this API, such as labs or deprecated. |
| `kind` | `string` | The kind for this response. |
| `version` | `string` | The version of the API. |
| `discoveryRestUrl` | `string` | The URL for the discovery REST document. |
| `title` | `string` | The title of this API. |
| `documentationLink` | `string` | A link to human readable documentation for the API. |
| `icons` | `object` | Links to 16x16 and 32x32 icons representing the API. |
| `discoveryLink` | `string` | A link to the discovery document. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Retrieve the list of APIs supported at this endpoint. |
| `getRest` | `EXEC` | `api, version` | Retrieve the description of a particular version of an api. |
