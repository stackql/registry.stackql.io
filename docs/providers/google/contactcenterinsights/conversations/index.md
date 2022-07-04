---
title: conversations
hide_title: false
hide_table_of_contents: false
keywords:
  - conversations
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
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.conversations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation} |
| `startTime` | `string` | The time at which the conversation started. |
| `turnCount` | `integer` | Output only. The number of turns in the conversation. |
| `runtimeAnnotations` | `array` | Output only. The annotations that were generated during the customer and agent interaction. |
| `dataSource` | `object` | The conversation source, which is a combination of transcript and audio. |
| `obfuscatedUserId` | `string` | Obfuscated user ID which the customer sent to us. |
| `agentId` | `string` | An opaque, user-specified string representing the human agent who handled the conversation. |
| `createTime` | `string` | Output only. The time at which the conversation was created. |
| `latestAnalysis` | `object` | The analysis resource. |
| `languageCode` | `string` | A user-specified language code for the conversation. |
| `labels` | `object` | A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry. |
| `duration` | `string` | Output only. The duration of the conversation. |
| `callMetadata` | `object` | Call-specific metadata. |
| `ttl` | `string` | Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time. |
| `updateTime` | `string` | Output only. The most recent time at which the conversation was updated. |
| `dialogflowIntents` | `object` | Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent} |
| `transcript` | `object` | A message representing the transcript of a conversation. |
| `expireTime` | `string` | The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted. |
| `medium` | `string` | Immutable. The conversation medium, if unspecified will default to PHONE_CALL. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_conversations_get` | `SELECT` | `name` | Gets a conversation. |
| `projects_locations_conversations_list` | `SELECT` | `parent` | Lists conversations. |
| `projects_locations_conversations_create` | `INSERT` | `parent` | Creates a conversation. |
| `projects_locations_conversations_delete` | `DELETE` | `name` | Deletes a conversation. |
| `projects_locations_conversations_calculateStats` | `EXEC` | `location` | Gets conversation statistics. |
| `projects_locations_conversations_patch` | `EXEC` | `name` | Updates a conversation. |
