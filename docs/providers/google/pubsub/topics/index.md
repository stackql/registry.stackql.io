---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The name of the topic. It must have the format `"projects/{project}/topics/{topic}"`. `{topic}` must start with a letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or percent signs (`%`). It must be between 3 and 255 characters in length, and it must not start with `"goog"`. |
| `schemaSettings` | `object` | Settings for validating messages published against a schema. |
| `kmsKeyName` | `string` | The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. The expected format is `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| `labels` | `object` | See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels). |
| `messageRetentionDuration` | `string` | Indicates the minimum duration to retain a message after it is published to the topic. If this field is set, messages published to the topic in the last `message_retention_duration` are always available to subscribers. For instance, it allows any attached subscription to [seek to a timestamp](https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time) that is up to `message_retention_duration` in the past. If this field is not set, message retention is controlled by settings on individual subscriptions. Cannot be more than 31 days or less than 10 minutes. |
| `messageStoragePolicy` | `object` | A policy constraining the storage of messages published to the topic. |
| `satisfiesPzs` | `boolean` | Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_topics_get` | `SELECT` | `topic` | Gets the configuration of a topic. |
| `projects_topics_list` | `SELECT` | `project` | Lists matching topics. |
| `projects_topics_create` | `INSERT` | `name` | Creates the given topic with the given name. See the [resource name rules] (https://cloud.google.com/pubsub/docs/admin#resource_names). |
| `projects_topics_delete` | `DELETE` | `topic` | Deletes the topic with the given name. Returns `NOT_FOUND` if the topic does not exist. After a topic is deleted, a new topic may be created with the same name; this is an entirely new topic with none of the old configuration or subscriptions. Existing subscriptions to this topic are not deleted, but their `topic` field is set to `_deleted-topic_`. |
| `projects_topics_patch` | `EXEC` | `name` | Updates an existing topic. Note that certain properties of a topic are not modifiable. |
| `projects_topics_publish` | `EXEC` | `topic` | Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic does not exist. |