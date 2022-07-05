---
title: inspect_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - inspect_templates
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
<tr><td><b>Name</b></td><td><code>inspect_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.inspect_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`; |
| `description` | `string` | Short description (max 256 chars). |
| `createTime` | `string` | Output only. The creation timestamp of an inspectTemplate. |
| `displayName` | `string` | Display name (max 256 chars). |
| `inspectConfig` | `object` | Configuration description of the scanning process. When used with redactContent only info_types and min_likelihood are currently used. |
| `updateTime` | `string` | Output only. The last update timestamp of an inspectTemplate. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_inspectTemplates_get` | `SELECT` | `name` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspectTemplates_list` | `SELECT` | `parent` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspectTemplates_get` | `SELECT` | `name` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspectTemplates_list` | `SELECT` | `parent` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspectTemplates_get` | `SELECT` | `name` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspectTemplates_list` | `SELECT` | `parent` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspectTemplates_get` | `SELECT` | `name` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspectTemplates_list` | `SELECT` | `parent` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspectTemplates_create` | `INSERT` | `parent` | Creates an InspectTemplate for re-using frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspectTemplates_create` | `INSERT` | `parent` | Creates an InspectTemplate for re-using frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspectTemplates_create` | `INSERT` | `parent` | Creates an InspectTemplate for re-using frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspectTemplates_create` | `INSERT` | `parent` | Creates an InspectTemplate for re-using frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspectTemplates_delete` | `DELETE` | `name` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspectTemplates_delete` | `DELETE` | `name` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspectTemplates_delete` | `DELETE` | `name` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspectTemplates_delete` | `DELETE` | `name` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspectTemplates_patch` | `EXEC` | `name` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspectTemplates_patch` | `EXEC` | `name` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspectTemplates_patch` | `EXEC` | `name` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspectTemplates_patch` | `EXEC` | `name` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
