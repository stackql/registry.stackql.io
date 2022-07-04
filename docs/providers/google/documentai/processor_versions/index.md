---
title: processor_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - processor_versions
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
<tr><td><b>Name</b></td><td><code>processor_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.processor_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}` |
| `createTime` | `string` | The time the processor version was created. |
| `deprecationInfo` | `object` | Information about the upcoming deprecation of this processor version. |
| `displayName` | `string` | The display name of the processor version. |
| `googleManaged` | `boolean` | Denotes that this ProcessorVersion is managed by google. |
| `kmsKeyName` | `string` | The KMS key name used for encryption. |
| `kmsKeyVersionName` | `string` | The KMS key version with which data is encrypted. |
| `state` | `string` | The state of the processor version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_processorVersions_get` | `SELECT` | `name` | Gets a processor version detail. |
| `projects_locations_processors_processorVersions_list` | `SELECT` | `parent` | Lists all versions of a processor. |
| `projects_locations_processors_processorVersions_delete` | `DELETE` | `name` | Deletes the processor version, all artifacts under the processor version will be deleted. |
| `projects_locations_processors_processorVersions_batchProcess` | `EXEC` | `name` | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| `projects_locations_processors_processorVersions_deploy` | `EXEC` | `name` | Deploys the processor version. |
| `projects_locations_processors_processorVersions_process` | `EXEC` | `name` | Processes a single document. |
| `projects_locations_processors_processorVersions_undeploy` | `EXEC` | `name` | Undeploys the processor version. |