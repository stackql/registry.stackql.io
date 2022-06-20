---
title: projects.locations.dlpJobs
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
<tr><td><b>Name</b></td><td><code>projects.locations.dlpJobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.projects.locations.dlpJobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The standard List next-page token. |
| `jobs` | `array` | A list of DlpJobs that matches the specified filter in the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dlpJobsId, locationsId, projectsId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| `delete` | `DELETE` | `dlpJobsId, locationsId, projectsId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `cancel` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `finish` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run. |
| `hybridInspect` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger. |
