---
title: specs
hide_title: false
hide_table_of_contents: false
keywords:
  - specs
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
<tr><td><b>Name</b></td><td><code>specs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.specs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. |
| `description` | `string` | A detailed description. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the spec. A new revision is committed whenever the spec contents are changed. The format is an 8-character hexadecimal string. |
| `filename` | `string` | A possibly-hierarchical name used to refer to the spec from other specs. |
| `hash` | `string` | Output only. A SHA-256 hash of the spec's contents. If the spec is gzipped, this is the hash of the uncompressed spec. |
| `revisionCreateTime` | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
| `createTime` | `string` | Output only. Creation timestamp; when the spec resource was created. |
| `mimeType` | `string` | A style (format) descriptor for this spec that is specified as a Media Type (https://en.wikipedia.org/wiki/Media_type). Possible values include "application/vnd.apigee.proto", "application/vnd.apigee.openapi", and "application/vnd.apigee.graphql", with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip"). |
| `sizeBytes` | `integer` | Output only. The size of the spec file in bytes. If the spec is gzipped, this is the size of the uncompressed spec. |
| `contents` | `string` | Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents. |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed. |
| `sourceUri` | `string` | The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved. |
| `revisionUpdateTime` | `string` | Output only. Last update timestamp: when the represented revision was last modified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_versions_specs_get` | `SELECT` | `name` | GetApiSpec returns a specified spec. |
| `projects_locations_apis_versions_specs_list` | `SELECT` | `parent` | ListApiSpecs returns matching specs. |
| `projects_locations_apis_versions_specs_create` | `INSERT` | `parent` | CreateApiSpec creates a specified spec. |
| `projects_locations_apis_versions_specs_delete` | `DELETE` | `name` | DeleteApiSpec removes a specified spec, all revisions, and all child resources (e.g. artifacts). |
| `projects_locations_apis_versions_specs_patch` | `EXEC` | `name` | UpdateApiSpec can be used to modify a specified spec. |
| `projects_locations_apis_versions_specs_rollback` | `EXEC` | `name` | RollbackApiSpec sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| `projects_locations_apis_versions_specs_tagRevision` | `EXEC` | `name` | TagApiSpecRevision adds a tag to a specified revision of a spec. |