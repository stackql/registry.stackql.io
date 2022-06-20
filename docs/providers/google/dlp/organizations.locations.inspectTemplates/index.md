---
title: organizations.locations.inspectTemplates
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
<tr><td><b>Name</b></td><td><code>organizations.locations.inspectTemplates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.organizations.locations.inspectTemplates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If the next page is available then the next page token to be used in following ListInspectTemplates request. |
| `inspectTemplates` | `array` | List of inspectTemplates, up to page_size in ListInspectTemplatesRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inspectTemplatesId, locationsId, organizationsId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `list` | `SELECT` | `locationsId, organizationsId` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `create` | `INSERT` | `locationsId, organizationsId` | Creates an InspectTemplate for re-using frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `delete` | `DELETE` | `inspectTemplatesId, locationsId, organizationsId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `patch` | `EXEC` | `inspectTemplatesId, locationsId, organizationsId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |