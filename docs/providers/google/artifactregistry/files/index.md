---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the file, for example: "projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt". If the file ID part contains slashes, they are escaped. |
| `hashes` | `array` | The hashes of the file content. |
| `owner` | `string` | The name of the Package or Version that owns this file, if any. |
| `sizeBytes` | `string` | The size of the File in bytes. |
| `updateTime` | `string` | The time when the File was last updated. |
| `createTime` | `string` | The time when the File was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_files_get` | `SELECT` | `name` | Gets a file. |
| `projects_locations_repositories_files_list` | `SELECT` | `parent` | Lists files. |
