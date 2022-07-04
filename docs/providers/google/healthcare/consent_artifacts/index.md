---
title: consent_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - consent_artifacts
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
<tr><td><b>Name</b></td><td><code>consent_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.consent_artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the Consent artifact, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. Cannot be changed after creation. |
| `consentContentScreenshots` | `array` | Optional. Screenshots, PDFs, or other binary information documenting the user's consent. |
| `consentContentVersion` | `string` | Optional. An string indicating the version of the consent information shown to the user. |
| `guardianSignature` | `object` | User signature. |
| `metadata` | `object` | Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `userSignature` | `object` | User signature. |
| `witnessSignature` | `object` | User signature. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_consentStores_consentArtifacts_get` | `SELECT` | `name` | Gets the specified Consent artifact. |
| `projects_locations_datasets_consentStores_consentArtifacts_list` | `SELECT` | `parent` | Lists the Consent artifacts in the specified consent store. |
| `projects_locations_datasets_consentStores_consentArtifacts_create` | `INSERT` | `parent` | Creates a new Consent artifact in the parent consent store. |
| `projects_locations_datasets_consentStores_consentArtifacts_delete` | `DELETE` | `name` | Deletes the specified Consent artifact. Fails if the artifact is referenced by the latest revision of any Consent. |