---
title: channels
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.youtube.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the channel. |
| `contentDetails` | `object` | Details about the content of a channel. |
| `status` | `object` | JSON template for the status part of a channel. |
| `contentOwnerDetails` | `object` | The contentOwnerDetails object encapsulates channel data that is relevant for YouTube Partners linked with the channel. |
| `etag` | `string` | Etag of this resource. |
| `conversionPings` | `object` | The conversionPings object encapsulates information about conversion pings that need to be respected by the channel. |
| `brandingSettings` | `object` | Branding properties of a YouTube channel. |
| `auditDetails` | `object` | The auditDetails object encapsulates channel data that is relevant for YouTube Partners during the audit process. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#channel". |
| `snippet` | `object` | Basic details about a channel, including title, description and thumbnails. |
| `statistics` | `object` | Statistics about a channel: number of subscribers, number of videos in the channel, etc. |
| `topicDetails` | `object` | Freebase topic information related to the channel. |
| `localizations` | `object` | Localizations for different languages |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `update` | `EXEC` | `part` | Updates an existing resource. |
