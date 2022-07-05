---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the version, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/art1". If the package or version ID parts contain slashes, the slashes are escaped. |
| `description` | `string` | Optional. Description of the version, as specified in its metadata. |
| `updateTime` | `string` | The time when the version was last updated. |
| `createTime` | `string` | The time when the version was created. |
| `metadata` | `object` | Output only. Repository-specific Metadata stored against this version. The fields returned are defined by the underlying repository-specific resource. Currently, the only resource in use is DockerImage |
| `relatedTags` | `array` | Output only. A list of related tags. Will contain up to 100 tags that reference this version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_packages_versions_get` | `SELECT` | `name` | Gets a version |
| `projects_locations_repositories_packages_versions_list` | `SELECT` | `parent` | Lists versions. |
| `projects_locations_repositories_packages_versions_delete` | `DELETE` | `name` | Deletes a version and all of its content. The returned operation will complete once the version has been deleted. |
