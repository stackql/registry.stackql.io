---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
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
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the repository, for example: "projects/p1/locations/us-central1/repositories/repo1". |
| `description` | `string` | The user-provided description of the repository. |
| `format` | `string` | The format of packages that are stored in the repository. |
| `createTime` | `string` | The time when the repository was created. |
| `labels` | `object` | Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes. |
| `mavenConfig` | `object` | MavenRepositoryConfig is maven related repository details. Provides additional configuration details for repositories of the maven format type. |
| `updateTime` | `string` | The time when the repository was last updated. |
| `kmsKeyName` | `string` | The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created. |
| `sizeBytes` | `string` | Output only. The size, in bytes, of all artifact storage in this repository. Repositories that are generally available or in public preview use this to calculate storage costs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_get` | `SELECT` | `name` | Gets a repository. |
| `projects_locations_repositories_list` | `SELECT` | `parent` | Lists repositories. |
| `projects_locations_repositories_create` | `INSERT` | `parent` | Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository. |
| `projects_locations_repositories_delete` | `DELETE` | `name` | Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response. |
| `projects_locations_repositories_patch` | `EXEC` | `name` | Updates a repository. |
