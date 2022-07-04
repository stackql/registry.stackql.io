---
title: feedback_messages
hide_title: false
hide_table_of_contents: false
keywords:
  - feedback_messages
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
<tr><td><b>Name</b></td><td><code>feedback_messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.feedback_messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the feedback message in a feedback thread. Format: 'project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}' |
| `requesterFeedbackMetadata` | `object` | Metadata describing the feedback from the labeling task requester. |
| `body` | `string` | String content of the feedback. Maximum of 10000 characters. |
| `createTime` | `string` | Create time. |
| `image` | `string` | The image storing this feedback if the feedback is an image representing operator's comments. |
| `operatorFeedbackMetadata` | `object` | Metadata describing the feedback from the operator. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotatedDatasets_feedbackThreads_feedbackMessages_get` | `SELECT` | `name` | Get a FeedbackMessage object. |
| `projects_datasets_annotatedDatasets_feedbackThreads_feedbackMessages_list` | `SELECT` | `parent` | List FeedbackMessages with pagination. |
| `projects_datasets_annotatedDatasets_feedbackThreads_feedbackMessages_create` | `INSERT` | `parent` | Create a FeedbackMessage object. |
| `projects_datasets_annotatedDatasets_feedbackThreads_feedbackMessages_delete` | `DELETE` | `name` | Delete a FeedbackMessage. |
