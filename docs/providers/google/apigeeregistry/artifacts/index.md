---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. |
| `mimeType` | `string` | A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible "schema" parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip"). |
| `sizeBytes` | `integer` | Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact. |
| `updateTime` | `string` | Output only. Last update timestamp. |
| `contents` | `string` | Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents. |
| `createTime` | `string` | Output only. Creation timestamp. |
| `hash` | `string` | Output only. A SHA-256 hash of the artifact's contents. If the artifact is gzipped, this is the hash of the uncompressed artifact. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_artifacts_get` | `SELECT` | `name` | GetArtifact returns a specified artifact. |
| `projects_locations_apis_artifacts_list` | `SELECT` | `parent` | ListArtifacts returns matching artifacts. |
| `projects_locations_apis_deployments_artifacts_get` | `SELECT` | `name` | GetArtifact returns a specified artifact. |
| `projects_locations_apis_deployments_artifacts_list` | `SELECT` | `parent` | ListArtifacts returns matching artifacts. |
| `projects_locations_apis_versions_artifacts_get` | `SELECT` | `name` | GetArtifact returns a specified artifact. |
| `projects_locations_apis_versions_artifacts_list` | `SELECT` | `parent` | ListArtifacts returns matching artifacts. |
| `projects_locations_apis_versions_specs_artifacts_get` | `SELECT` | `name` | GetArtifact returns a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_list` | `SELECT` | `parent` | ListArtifacts returns matching artifacts. |
| `projects_locations_artifacts_get` | `SELECT` | `name` | GetArtifact returns a specified artifact. |
| `projects_locations_artifacts_list` | `SELECT` | `parent` | ListArtifacts returns matching artifacts. |
| `projects_locations_apis_artifacts_create` | `INSERT` | `parent` | CreateArtifact creates a specified artifact. |
| `projects_locations_apis_deployments_artifacts_create` | `INSERT` | `parent` | CreateArtifact creates a specified artifact. |
| `projects_locations_apis_versions_artifacts_create` | `INSERT` | `parent` | CreateArtifact creates a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_create` | `INSERT` | `parent` | CreateArtifact creates a specified artifact. |
| `projects_locations_artifacts_create` | `INSERT` | `parent` | CreateArtifact creates a specified artifact. |
| `projects_locations_apis_artifacts_delete` | `DELETE` | `name` | DeleteArtifact removes a specified artifact. |
| `projects_locations_apis_deployments_artifacts_delete` | `DELETE` | `name` | DeleteArtifact removes a specified artifact. |
| `projects_locations_apis_versions_artifacts_delete` | `DELETE` | `name` | DeleteArtifact removes a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_delete` | `DELETE` | `name` | DeleteArtifact removes a specified artifact. |
| `projects_locations_artifacts_delete` | `DELETE` | `name` | DeleteArtifact removes a specified artifact. |
| `projects_locations_apis_artifacts_replaceArtifact` | `EXEC` | `name` | ReplaceArtifact can be used to replace a specified artifact. |
| `projects_locations_apis_deployments_artifacts_replaceArtifact` | `EXEC` | `name` | ReplaceArtifact can be used to replace a specified artifact. |
| `projects_locations_apis_versions_artifacts_replaceArtifact` | `EXEC` | `name` | ReplaceArtifact can be used to replace a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_replaceArtifact` | `EXEC` | `name` | ReplaceArtifact can be used to replace a specified artifact. |
| `projects_locations_artifacts_replaceArtifact` | `EXEC` | `name` | ReplaceArtifact can be used to replace a specified artifact. |
