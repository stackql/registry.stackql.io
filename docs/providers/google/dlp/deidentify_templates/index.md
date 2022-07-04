---
title: deidentify_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - deidentify_templates
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
<tr><td><b>Name</b></td><td><code>deidentify_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.deidentify_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID` |
| `description` | `string` | Short description (max 256 chars). |
| `displayName` | `string` | Display name (max 256 chars). |
| `updateTime` | `string` | Output only. The last update timestamp of an inspectTemplate. |
| `createTime` | `string` | Output only. The creation timestamp of an inspectTemplate. |
| `deidentifyConfig` | `object` | The configuration that controls how the data will change. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_deidentifyTemplates_get` | `SELECT` | `name` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentifyTemplates_list` | `SELECT` | `parent` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentifyTemplates_get` | `SELECT` | `name` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentifyTemplates_list` | `SELECT` | `parent` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentifyTemplates_get` | `SELECT` | `name` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentifyTemplates_list` | `SELECT` | `parent` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentifyTemplates_get` | `SELECT` | `name` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentifyTemplates_list` | `SELECT` | `parent` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentifyTemplates_create` | `INSERT` | `parent` | Creates a DeidentifyTemplate for re-using frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentifyTemplates_create` | `INSERT` | `parent` | Creates a DeidentifyTemplate for re-using frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentifyTemplates_create` | `INSERT` | `parent` | Creates a DeidentifyTemplate for re-using frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentifyTemplates_create` | `INSERT` | `parent` | Creates a DeidentifyTemplate for re-using frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentifyTemplates_delete` | `DELETE` | `name` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentifyTemplates_delete` | `DELETE` | `name` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentifyTemplates_delete` | `DELETE` | `name` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentifyTemplates_delete` | `DELETE` | `name` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentifyTemplates_patch` | `EXEC` | `name` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentifyTemplates_patch` | `EXEC` | `name` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentifyTemplates_patch` | `EXEC` | `name` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentifyTemplates_patch` | `EXEC` | `name` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
