---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded. |
| `version` | `string` | The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_packages_tags_get` | `SELECT` | `name` | Gets a tag. |
| `projects_locations_repositories_packages_tags_list` | `SELECT` | `parent` | Lists tags. |
| `projects_locations_repositories_packages_tags_create` | `INSERT` | `parent` | Creates a tag. |
| `projects_locations_repositories_packages_tags_delete` | `DELETE` | `name` | Deletes a tag. |
| `projects_locations_repositories_packages_tags_patch` | `EXEC` | `name` | Updates a tag. |
