---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
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
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.transcoder.job_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the job template. Format: `projects/{project_number}/locations/{location}/jobTemplates/{job_template}` |
| `config` | `object` | Job configuration |
| `labels` | `object` | The labels associated with this job template. You can use these to organize and group your job templates. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobTemplates_get` | `SELECT` | `name` | Returns the job template data. |
| `projects_locations_jobTemplates_list` | `SELECT` | `parent` | Lists job templates in the specified region. |
| `projects_locations_jobTemplates_create` | `INSERT` | `parent` | Creates a job template in the specified region. |
| `projects_locations_jobTemplates_delete` | `DELETE` | `name` | Deletes a job template. |