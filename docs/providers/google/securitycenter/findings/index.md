---
title: findings
hide_title: false
hide_table_of_contents: false
keywords:
  - findings
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
<tr><td><b>Name</b></td><td><code>findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.findings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `finding` | `object` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding. |
| `resource` | `object` | Information related to the Google Cloud resource that is associated with this finding. |
| `stateChange` | `string` | State change of the finding between the points in time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_sources_findings_list` | `SELECT` | `parent` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings |
| `organizations_sources_findings_list` | `SELECT` | `parent` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings |
| `projects_sources_findings_list` | `SELECT` | `parent` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings |
| `organizations_sources_findings_create` | `INSERT` | `parent` | Creates a finding. The corresponding source must exist for finding creation to succeed. |
| `folders_findings_bulkMute` | `EXEC` | `parent` | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| `folders_sources_findings_group` | `EXEC` | `parent` | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings |
| `folders_sources_findings_patch` | `EXEC` | `name` | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| `folders_sources_findings_setMute` | `EXEC` | `name` | Updates the mute state of a finding. |
| `folders_sources_findings_setState` | `EXEC` | `name` | Updates the state of a finding. |
| `folders_sources_findings_updateSecurityMarks` | `EXEC` | `name` | Updates security marks. |
| `organizations_findings_bulkMute` | `EXEC` | `parent` | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| `organizations_sources_findings_group` | `EXEC` | `parent` | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings |
| `organizations_sources_findings_patch` | `EXEC` | `name` | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| `organizations_sources_findings_setMute` | `EXEC` | `name` | Updates the mute state of a finding. |
| `organizations_sources_findings_setState` | `EXEC` | `name` | Updates the state of a finding. |
| `organizations_sources_findings_updateSecurityMarks` | `EXEC` | `name` | Updates security marks. |
| `projects_findings_bulkMute` | `EXEC` | `parent` | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| `projects_sources_findings_group` | `EXEC` | `parent` | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings |
| `projects_sources_findings_patch` | `EXEC` | `name` | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| `projects_sources_findings_setMute` | `EXEC` | `name` | Updates the mute state of a finding. |
| `projects_sources_findings_setState` | `EXEC` | `name` | Updates the state of a finding. |
| `projects_sources_findings_updateSecurityMarks` | `EXEC` | `name` | Updates security marks. |
