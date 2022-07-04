---
title: phrase_matchers
hide_title: false
hide_table_of_contents: false
keywords:
  - phrase_matchers
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
<tr><td><b>Name</b></td><td><code>phrase_matchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.phrase_matchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher} |
| `phraseMatchRuleGroups` | `array` | A list of phase match rule groups that are included in this matcher. |
| `updateTime` | `string` | Output only. The most recent time at which the phrase matcher was updated. |
| `activationUpdateTime` | `string` | Output only. The most recent time at which the activation status was updated. |
| `displayName` | `string` | The human-readable name of the phrase matcher. |
| `versionTag` | `string` | The customized version tag to use for the phrase matcher. If not specified, it will default to `revision_id`. |
| `type` | `string` | Required. The type of this phrase matcher. |
| `active` | `boolean` | Applies the phrase matcher only when it is active. |
| `roleMatch` | `string` | The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript. |
| `revisionCreateTime` | `string` | Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567 |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_phraseMatchers_get` | `SELECT` | `name` | Gets a phrase matcher. |
| `projects_locations_phraseMatchers_list` | `SELECT` | `parent` | Lists phrase matchers. |
| `projects_locations_phraseMatchers_create` | `INSERT` | `parent` | Creates a phrase matcher. |
| `projects_locations_phraseMatchers_delete` | `DELETE` | `name` | Deletes a phrase matcher. |
| `projects_locations_phraseMatchers_patch` | `EXEC` | `name` | Updates a phrase matcher. |