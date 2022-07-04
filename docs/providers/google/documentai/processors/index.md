---
title: processors
hide_title: false
hide_table_of_contents: false
keywords:
  - processors
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
<tr><td><b>Name</b></td><td><code>processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.documentai.processors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Immutable. The resource name of the processor. Format: `projects/{project}/locations/{location}/processors/{processor}` |
| `state` | `string` | Output only. The state of the processor. |
| `type` | `string` | The processor type, e.g., OCR_PROCESSOR, INVOICE_PROCESSOR, etc. To get a list of processors types, see FetchProcessorTypes. |
| `createTime` | `string` | The time the processor was created. |
| `defaultProcessorVersion` | `string` | The default processor version. |
| `displayName` | `string` | The display name of the processor. |
| `kmsKeyName` | `string` | The KMS key used for encryption/decryption in CMEK scenarios. See https://cloud.google.com/security-key-management. |
| `processEndpoint` | `string` | Output only. Immutable. The http endpoint that can be called to invoke processing. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_processors_get` | `SELECT` | `name` | Gets a processor detail. |
| `projects_locations_processors_list` | `SELECT` | `parent` | Lists all processors which belong to this project. |
| `projects_locations_processors_create` | `INSERT` | `parent` | Creates a processor from the type processor that the user chose. The processor will be at "ENABLED" state by default after its creation. |
| `projects_locations_processors_delete` | `DELETE` | `name` | Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor. |
| `projects_locations_processors_batchProcess` | `EXEC` | `name` | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| `projects_locations_processors_disable` | `EXEC` | `name` | Disables a processor |
| `projects_locations_processors_enable` | `EXEC` | `name` | Enables a processor |
| `projects_locations_processors_process` | `EXEC` | `name` | Processes a single document. |
| `projects_locations_processors_setDefaultProcessorVersion` | `EXEC` | `processor` | Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments. |
