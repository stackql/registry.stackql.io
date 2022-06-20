---
title: projects.locations.jobTriggers
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
<tr><td><b>Name</b></td><td><code>projects.locations.jobTriggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.projects.locations.jobTriggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If the next page is available then the next page token to be used in following ListJobTriggers request. |
| `jobTriggers` | `array` | List of triggeredJobs, up to page_size in ListJobTriggersRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobTriggersId, locationsId, projectsId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `delete` | `DELETE` | `jobTriggersId, locationsId, projectsId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `activate` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| `hybridInspect` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger. |
| `patch` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |