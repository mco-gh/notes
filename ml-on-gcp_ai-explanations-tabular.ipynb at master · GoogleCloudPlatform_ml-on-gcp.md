ml-on-gcp/ai-explanations-tabular.ipynb at master · GoogleCloudPlatform/ml-on-gcp

 [Skip to content](https://github.com/GoogleCloudPlatform/ml-on-gcp/blob/master/tutorials/explanations/ai-explanations-tabular.ipynb#start-of-content)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-mark-github v-align-middle js-evernote-checked' height='32' viewBox='0 0 16 16' version='1.1' width='32' aria-hidden='true' data-evernote-id='0'%3e%3cpath fill-rule='evenodd' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z' data-evernote-id='319' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/)

   ![68747470733a2f2f636c6f75642e676f6f676c652e636f6d2f6d6c2d656e67696e652f696d616765732f636f6c61622d6c6f676f2d333270782e706e67](../_resources/7f276b97d50cd5060a3ab35d484b041b.png)

 [Pull requests](https://github.com/pulls)  [Issues](https://github.com/issues)

 [Marketplace](https://github.com/marketplace)
 [Explore](https://github.com/explore)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-bell js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='13'%3e%3cpath fill-rule='evenodd' d='M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z' data-evernote-id='378' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)You have no unread notifications](https://github.com/notifications/beta)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-plus js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true' data-evernote-id='14'%3e%3cpath fill-rule='evenodd' d='M12 9H7v5H5V9H0V7h5V2h2v5h5v2z' data-evernote-id='380' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

 ![658327](../_resources/7ed50c64c61ceafc0466928a529ced19.jpg)

#   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-repo js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true' data-evernote-id='18'%3e%3cpath fill-rule='evenodd' d='M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z' data-evernote-id='465' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)    [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)    /  **  [ml-on-gcp](https://github.com/GoogleCloudPlatform/ml-on-gcp)  **

-

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-eye v-align-text-bottom js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='19'%3e%3cpath fill-rule='evenodd' d='M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z' data-evernote-id='472' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Watch

 [59](https://github.com/GoogleCloudPlatform/ml-on-gcp/watchers)

- [298](https://github.com/GoogleCloudPlatform/ml-on-gcp/stargazers)

- ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-repo-forked v-align-text-bottom js-evernote-checked' viewBox='0 0 10 16' version='1.1' width='10' height='16' aria-hidden='true' data-evernote-id='30'%3e%3cpath fill-rule='evenodd' d='M8 1a1.993 1.993 0 00-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 002 1a1.993 1.993 0 00-1 3.72V6.5l3 3v1.78A1.993 1.993 0 005 15a1.993 1.993 0 001-3.72V9.5l3-3V4.72A1.993 1.993 0 008 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z' data-evernote-id='508' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Fork

 [114](https://github.com/GoogleCloudPlatform/ml-on-gcp/network/members)

   [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-code js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='32'%3e%3cpath fill-rule='evenodd' d='M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z' data-evernote-id='519' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)   Code](https://github.com/GoogleCloudPlatform/ml-on-gcp)      [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-issue-opened js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='33'%3e%3cpath fill-rule='evenodd' d='M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 011.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z' data-evernote-id='524' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)   Issues  4](https://github.com/GoogleCloudPlatform/ml-on-gcp/issues)      [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-git-pull-request js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true' data-evernote-id='34'%3e%3cpath fill-rule='evenodd' d='M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z' data-evernote-id='530' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)   Pull requests  1](https://github.com/GoogleCloudPlatform/ml-on-gcp/pulls)      [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-play js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='35'%3e%3cpath fill-rule='evenodd' d='M14 8A7 7 0 110 8a7 7 0 0114 0zm-8.223 3.482l4.599-3.066a.5.5 0 000-.832L5.777 4.518A.5.5 0 005 4.934v6.132a.5.5 0 00.777.416z' data-evernote-id='536' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Actions](https://github.com/GoogleCloudPlatform/ml-on-gcp/actions)    [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-project js-evernote-checked' viewBox='0 0 15 16' version='1.1' width='15' height='16' aria-hidden='true' data-evernote-id='36'%3e%3cpath fill-rule='evenodd' d='M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z' data-evernote-id='538' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Projects 0](https://github.com/GoogleCloudPlatform/ml-on-gcp/projects)  [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-shield js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='37'%3e%3cpath fill-rule='evenodd' d='M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z' data-evernote-id='541' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Security](https://github.com/GoogleCloudPlatform/ml-on-gcp/security/advisories)  [ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-graph js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='38'%3e%3cpath fill-rule='evenodd' d='M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z' data-evernote-id='543' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Insights](https://github.com/GoogleCloudPlatform/ml-on-gcp/pulse)

 *Branch:*  master

##   [ml-on-gcp](https://github.com/GoogleCloudPlatform/ml-on-gcp)  /  [tutorials](https://github.com/GoogleCloudPlatform/ml-on-gcp/tree/master/tutorials)  /  [explanations](https://github.com/GoogleCloudPlatform/ml-on-gcp/tree/master/tutorials/explanations)  /  **ai-explanations-tabular.ipynb**

 [Find file](https://github.com/GoogleCloudPlatform/ml-on-gcp/find/master)   Copy path

   [![3814898](../_resources/1eede06eb9ab47642c45c2c16632d211.jpg)](https://github.com/sararob)  [sararob](https://github.com/sararob)    [Update XAI tabular sample (](https://github.com/GoogleCloudPlatform/ml-on-gcp/commit/76483fe461acc0bf03f609752c67fb9db2ad8a93)[#90](https://github.com/GoogleCloudPlatform/ml-on-gcp/pull/90)[)](https://github.com/GoogleCloudPlatform/ml-on-gcp/commit/76483fe461acc0bf03f609752c67fb9db2ad8a93)        [76483fe](https://github.com/GoogleCloudPlatform/ml-on-gcp/commit/76483fe461acc0bf03f609752c67fb9db2ad8a93)  21 days ago

 **2** contributors

   [![3814898](../_resources/1eede06eb9ab47642c45c2c16632d211.jpg)](https://github.com/GoogleCloudPlatform/ml-on-gcp/commits/master/tutorials/explanations/ai-explanations-tabular.ipynb?author=sararob)  [![7587635](../_resources/2f61af985c978442581e91875b1aafdc.jpg)](https://github.com/GoogleCloudPlatform/ml-on-gcp/commits/master/tutorials/explanations/ai-explanations-tabular.ipynb?author=dizcology)

1396 lines (1396 sloc)  44.9 KB

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-code js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='41'%3e%3cpath fill-rule='evenodd' d='M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z' data-evernote-id='613' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Display the source blob](https://github.com/GoogleCloudPlatform/ml-on-gcp/blob/master/tutorials/explanations/ai-explanations-tabular.ipynb?short_path=2a4922d)  [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-file js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true' data-evernote-id='42'%3e%3cpath fill-rule='evenodd' d='M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z' data-evernote-id='614' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Display the rendered blob](https://github.com/GoogleCloudPlatform/ml-on-gcp/blob/master/tutorials/explanations/ai-explanations-tabular.ipynb)

 [Raw](https://github.com/GoogleCloudPlatform/ml-on-gcp/raw/master/tutorials/explanations/ai-explanations-tabular.ipynb)  [Blame](https://github.com/GoogleCloudPlatform/ml-on-gcp/blame/master/tutorials/explanations/ai-explanations-tabular.ipynb)  [History](https://github.com/GoogleCloudPlatform/ml-on-gcp/commits/master/tutorials/explanations/ai-explanations-tabular.ipynb)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-device-desktop js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='43'%3e%3cpath fill-rule='evenodd' d='M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z' data-evernote-id='617' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)Open this file in GitHub Desktop](https://desktop.github.com/)

In [0]:

*# Copyright 2019 Google LLC**#**# Licensed under the Apache License, Version 2.0 (the "License");**# you may not use this file except in compliance with the License.**# You may obtain a copy of the License at**#**# https://www.apache.org/licenses/LICENSE-2.0**#**# Unless required by applicable law or agreed to in writing, software**# distributed under the License is distributed on an "AS IS" BASIS,**# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.**# See the License for the specific language governing permissions and**# limitations under the License.*

# AI Explanations: Explaining a tabular data model[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#AI-Explanations:-Explaining-a-tabular-data-model)

|     |     |
| --- | --- |
|  [![68747470733a2f2f636c6f75642e676f6f676c652e636f6d2f6d6c2d656e67696e652f696d616765732f6769746875622d6c6f676f2d333270782e706e67](../_resources/d4a2655b6f4d40a71fcdd856cf064004.png) Run in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/ml-on-gcp/blob/master/tutorials/explanations/ai-explanations-tabular.ipynb) |  [![search-key-slash.png](../_resources/be13b3766ab88fa7760967facdbdc601.png) View on GitHub](https://github.com/GoogleCloudPlatform/ml-on-gcp/tree/master/tutorials/explanations/ai-explanations-tabular.ipynb) |

## Overview[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Overview)

This tutorial shows how to train a Keras model on tabular data and deploy it to the AI Explanations service to get feature attributions on your deployed model.

If you've already got a trained model and want to deploy it to AI Explanations, skip to the **Export the model as a TF 1 SavedModel** section.

### Dataset[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Dataset)

The dataset used for this tutorial was created by combining two BigQuery Public Datasets: [London Bikeshare data](https://console.cloud.google.com/marketplace/details/greater-london-authority/london-bicycles?filter=solution-type%3Adataset&q=london%20bicycle%20hires&id=95374cac-2834-4fa2-a71f-fc033ccb5ce4) and [NOAA weather data](https://console.cloud.google.com/marketplace/details/noaa-public/gsod?filter=solution-type:dataset&q=noaa&id=c6c1b652-3958-4a47-9e58-552a546df47f).

### Objective[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Objective)

The goal is to train a model using the Keras Sequential API that predicts how long a bike trip took based on the trip start time, distance, day of week, and various weather data during that day.

This tutorial focuses more on deploying the model to AI Explanations than on the design of the model itself.

### Costs[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Costs)

This tutorial uses billable components of Google Cloud Platform (GCP):

- AI Platform for:
    - Prediction
    - Explanation: AI Explanations comes at no extra charge to prediction prices. However, explanation requests take longer to process than normal predictions, so heavy usage of AI Explanations along with auto-scaling may result in more nodes being started and thus more charges
- Cloud Storage for:
    - Storing model files for deploying to Cloud AI Platform

Learn about [AI Platform pricing](https://cloud.google.com/ml-engine/docs/pricing) and [Cloud Storage pricing](https://cloud.google.com/storage/pricing), and use the [Pricing Calculator](https://cloud.google.com/products/calculator/)to generate a cost estimate based on your projected usage.

## Before you begin[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Before-you-begin)

Make sure you're running this notebook in a **GPU runtime** if you have that option. In Colab, select **Runtime** --> **Change runtime type**

This tutorial assumes you are running the notebook either in **Colab** or **Cloud AI Platform Notebooks**.

### Set up your GCP project[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Set-up-your-GCP-project)

**The following steps are required, regardless of your notebook environment.**

1. [Select or create a GCP project.](https://console.cloud.google.com/cloud-resource-manager)

2. [Make sure that billing is enabled for your project.](https://cloud.google.com/billing/docs/how-to/modify-project)

3. [Enable the AI Platform Training & Prediction and Compute Engine APIs.](https://console.cloud.google.com/flows/enableapi?apiid=ml.googleapis.com,compute_component)

4. Enter your project ID in the cell below. Then run the cell to make sure the Cloud SDK uses the right project for all the commands in this notebook.

**Note**: Jupyter runs lines prefixed with `!` as shell commands, and it interpolates Python variables prefixed with `$` into these commands.

In [0]:

PROJECT_ID  =  "<your-project-id>"

### Authenticate your GCP account[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Authenticate-your-GCP-account)

**If you are using AI Platform Notebooks**, your environment is already authenticated. Skip this step.

**If you are using Colab**, run the cell below and follow the instructions when prompted to authenticate your account via oAuth.

In [0]:

import  sys,  osimport  warningswarnings.filterwarnings('ignore')os.environ['TF_CPP_MIN_LOG_LEVEL']  =  '3'  *# If you are running this notebook in Colab, follow the**# instructions to authenticate your GCP account. This provides access to your**# Cloud Storage bucket and lets you submit training jobs and prediction**# requests.*if  'google.colab'  in  sys.modules:  from  google.colab  import  auth  as  google_auth  google_auth.authenticate_user()  !pip  install  witwidget  --quiet  !pip  install  tensorflow==1.15.0  --quiet  !gcloud  config  set  project  $PROJECT_IDelif  "DL_PATH"  in  os.environ:  !sudo  pip  install  tabulate  --quiet

### Create a Cloud Storage bucket[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Create-a-Cloud-Storage-bucket)

**The following steps are required, regardless of your notebook environment.**

When you submit a training job using the Cloud SDK, you upload a Python package containing your training code to a Cloud Storage bucket. AI Platform runs the code from this package. In this tutorial, AI Platform also saves the trained model that results from your job in the same bucket. You can then create an AI Platform model version based on this output in order to serve online predictions.

Set the name of your Cloud Storage bucket below. It must be unique across all Cloud Storage buckets.

You may also change the `REGION` variable, which is used for operations throughout the rest of this notebook. Make sure to [choose a region where Cloud AI Platform services are available](https://cloud.google.com/ml-engine/docs/tensorflow/regions). You may not use a Multi-Regional Storage bucket for training with AI Platform.

In [0]:

BUCKET_NAME  =  "<your-bucket-name>"REGION  =  "us-central1"

**Only if your bucket doesn't already exist**: Run the following cell to create your Cloud Storage bucket.

In [0]:

!gsutil  mb  -l  $REGION  gs://$BUCKET_NAME

### Import libraries[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Import-libraries)

Import the libraries we'll be using in this tutorial. This tutorial has been tested with **TensorFlow versions 1.14 and 1.15**.

In [0]:

import  tensorflow  as  tf  import  pandas  as  pdimport  numpy  as  np  import  jsonimport  timefrom  sklearn.preprocessing  import  LabelEncoderfrom  sklearn.preprocessing  import  MinMaxScalerfrom  tabulate  import  tabulate*# Should be 1.15.0*print(tf.__version__)

## Downloading and preprocessing data[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Downloading-and-preprocessing-data)

In this section you'll download the data to train your model from a public GCS bucket. The original data is from the BigQuery datasets linked above. For your convenience, we've joined the London bike and NOAA weather tables, done some preprocessing, and provided a subset of that dataset here.

In [0]:

*# Copy the data to your notebook instance*!gsutil  cp  'gs://explanations_sample_data/bike-data.csv'  ./

### Read the data with Pandas[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Read-the-data-with-Pandas)

We'll use Pandas to read the data into a `DataFrame` and then do some additional pre-processing.

In [0]:

data  =  pd.read_csv('bike-data.csv')*# Shuffle the data*data  =  data.sample(frac=1,  random_state=2)*# Drop rows with null values*data  =  data[data['wdsp']  !=  999.9]data  =  data[data['dewp']  !=  9999.9]*# Rename some columns for readability*data=data.rename(columns  =  {'day_of_week':'weekday'})data=data.rename(columns  =  {'max':'max_temp'})data=data.rename(columns  =  {'dewp':  'dew_point'})*# Drop columns we won't use to train this model*data  =  data.drop(columns=['start_station_name',  'end_station_name',  'bike_id',  'snow_ice_pellets'])*# Convert trip duration from seconds to minutes so it's easier to understand*data['duration']  =  data['duration'].apply(lambda  x:float(x  /  60))

In [0]:

*# Preview the first 5 rows*data.head()
In [0]:

*# Save duration to its own DataFrame and remove it from the original DataFrame*labels  =  data['duration']data  =  data.drop(columns=['duration'])

### Split data into train and test sets[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Split-data-into-train-and-test-sets)

We'll split our data into train and test sets using an 80 / 20 train / test split.

In [0]:

*# Use 80/20 train/test split*train_size  =  int(len(data)  *  .8)print  ("Train size: %d"  %  train_size)print  ("Test size: %d"  %  (len(data)  -  train_size))*# Split our data into train and test sets*train_data  =  data[:train_size]train_labels  =  labels[:train_size]test_data  =  data[train_size:]test_labels  =  labels[train_size:]

## Build, train, and evaluate our model with Keras[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Build,-train,-and-evaluate-our-model-with-Keras)

We'll use tf.keras to build a simple Sequential model that takes our 10 features as input and predicts trip duration in minutes (numerical value).

In [0]:

*# Build our model*model  =  tf.keras.Sequential(name="bike_predict")model.add(tf.keras.layers.Dense(64,  input_dim=len(train_data.iloc[0]),  activation='relu'))model.add(tf.keras.layers.Dense(32,  activation='relu'))model.add(tf.keras.layers.Dense(1))

In [0]:

*# Compile the model and see a summary*optimizer  =  tf.keras.optimizers.Adam(0.001)model.compile(loss='mean_squared_logarithmic_error',  optimizer=optimizer)model.summary()

### Create an input data pipeline with tf.data[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Create-an-input-data-pipeline-with-tf.data)

In [0]:

batch_size  =  256epochs  =  3input_train  =  tf.data.Dataset.from_tensor_slices(train_data)output_train  =  tf.data.Dataset.from_tensor_slices(train_labels)input_train  =  input_train.batch(batch_size).repeat()output_train  =  output_train.batch(batch_size).repeat()train_dataset  =  tf.data.Dataset.zip((input_train,  output_train))

### Train the model[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Train-the-model)

In [0]:

*# This will take about a minute to run**# To keep training time short, we're not using the full dataset*model.fit(train_dataset,  steps_per_epoch=train_size  //  batch_size,  epochs=epochs)

### Evaluate the trained model locally[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Evaluate-the-trained-model-locally)

In [0]:

*# Run evaluation*results  =  model.evaluate(test_data,  test_labels)print(results)

In [0]:

*# Send test instances to model for prediction*predict  =  model.predict(test_data[:5])

In [0]:

*# Preview predictions on the first 5 examples from our test dataset*for  i,  val  in  enumerate(predict):  print('Predicted duration: {}'.format(round(val[0])))  print('Actual duration: {}  \n'.format(test_labels.iloc[i]))

## Export the model as a TF 1 SavedModel[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Export-the-model-as-a-TF-1-SavedModel)

AI Explanations currently supports TensorFlow 1.x. In order to deploy our model in a format compatible with AI Explanations, we'll follow the steps below to convert our Keras model to a TF Estimator, and then use the `export_saved_model` method to generate the SavedModel and save it in GCS.

In [0]:

*## Convert our Keras model to an estimator*keras_estimator  =  tf.keras.estimator.model_to_estimator(keras_model=model,  model_dir='export')

In [0]:

*# We need this serving input function to export our model in the next cell*serving_fn  =  tf.estimator.export.build_raw_serving_input_receiver_fn(  {'dense_input':  model.input})

In [0]:

export_path  =  keras_estimator.export_saved_model(  'gs://'  +  BUCKET_NAME  +  '/explanations',  serving_input_receiver_fn=serving_fn).decode('utf-8')print(export_path)

Use TensorFlow's `saved_model_cli` to inspect the model's SignatureDef. We'll use this information when we deploy our model to AI Explanations in the next section.

In [0]:

!saved_model_cli  show  --dir  $export_path  --all

## Deploy the model to AI Explanations[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Deploy-the-model-to-AI-Explanations)

In order to deploy the model to Explanations, we need to generate an `explanations_metadata.json` file and upload this to the Cloud Storage bucket with our SavedModel. Then we'll deploy the model using `gcloud`.

### Prepare explanation metadata[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Prepare-explanation-metadata)

We need to tell AI Explanations the names of the input and output tensors our model is expecting, which we print below.

The value for `input_baselines` tells the explanations service what the baseline input should be for our model. Here we're using the median for all of our input features. That means the baseline prediction for this model will be the trip duration our model predicts for the median of each feature in our dataset.

Since this model accepts a single numpy array with all numerical feature, we can optionally pass an `index_feature_mapping` list to AI Explanations to make the API response easier to parse. When we provide a list of feature names via this parameter, the service will return a key / value mapping of each feature with its corresponding attribution value.

In [0]:

*# Print the names of our tensors*print('Model input tensor: ',  model.input.name)print('Model output tensor: ',  model.output.name)

In [0]:

explanation_metadata  =  {  "inputs":  {  "data":  {  "input_tensor_name":  model.input.name,  "input_baselines":  [train_data.median().values.tolist()],  "encoding":  "bag_of_features",  "index_feature_mapping":  train_data.columns.tolist()  }  },  "outputs":  {  "duration":  {  "output_tensor_name":  model.output.name  }  },  "framework":  "tensorflow"  }

Since this is a regression model (predicting a numerical value), the baseline prediction will be the same for every example we send to the model. If this were instead a classification model, each class would have a different baseline prediction.

In [0]:

*# Write the json to a local file*with  open('explanation_metadata.json',  'w')  as  output_file:  json.dump(explanation_metadata,  output_file)

In [0]:

!gsutil  cp  explanation_metadata.json  $export_path

### Create the model[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Create-the-model)

In [0]:

MODEL  =  'bike'
In [0]:

*# Create the model if it doesn't exist yet (you only need to run this once)*!gcloud  ai-platform  models  create  $MODEL  --enable-logging  --regions=us-central1

### Create the model version[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Create-the-model-version)

Creating the version will take ~5-10 minutes. Note that your first deploy may take longer.

In [0]:

*# Each time you create a version the name should be unique*VERSION  =  'v1'
In [0]:

*# Create the version with gcloud*explain_method  =  'integrated-gradients'!gcloud  beta  ai-platform  versions  create  $VERSION \--model  $MODEL \--origin  $export_path \--runtime-version  1.15 \--framework  TENSORFLOW \--python-version  3.7 \--machine-type  n1-standard-4 \--explanation-method  $explain_method \--num-integral-steps  25

In [0]:

*# Make sure the model deployed correctly. State should be `READY` in the following log*!gcloud  ai-platform  versions  describe  $VERSION  --model  $MODEL

## Getting predictions and explanations on deployed model[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Getting-predictions-and-explanations-on-deployed-model)

Now that your model is deployed, you can use the AI Platform Prediction API to get feature attributions. We'll pass it a single test example here and see which features were most important in the model's prediction. Here we'll use `gcloud` to call our deployed model.

### Format our request for gcloud[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Format-our-request-for-gcloud)

To use gcloud to make our AI Explanations request, we need to write the JSON to a file.

In [0]:

*# Format data for prediction to our model*prediction_json  =  {'dense_input':  test_data.iloc[0].values.tolist()}with  open('bike-data.txt',  'a')  as  outfile:  json.dump(prediction_json,  outfile)

In [0]:

*# Preview the contents of the data file*!cat  bike-data.txt

### Making the explain request[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Making-the-explain-request)

In [0]:

resp_obj  =  !gcloud  beta  ai-platform  explain  --model  $MODEL  --version  $VERSION  --json-instances='bike-data.txt'response  =  json.loads(resp_obj.s)

### Understanding the explanations response[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Understanding-the-explanations-response)

First, let's look at the trip duration our model predicted and compare it to the actual value

In [0]:

explanations  =  response['explanations'][0]['attributions_by_label'][0]predicted  =  round(explanations['example_score'],  2)print('Predicted duration: '  +  str(predicted)  +  ' minutes')print('Actual duration: '  +  str(test_labels.iloc[0])  +  ' minutes')

Next let's look at the feature attributions for this particular example. Positive attribution values mean a particular feature pushed our model prediction up by that amount, and vice versa for negative attribution values.

In [0]:

feature_names  =  test_data.columns.tolist()attributions  =  explanations['attributions']['data']rows  =  []for  i,val  in  enumerate(feature_names):  rows.append([val,  test_data.iloc[1].tolist()[i],  attributions[i]])print(tabulate(rows,headers=['Feature name',  'Feature value',  'Attribution value']))

## Sanity check our explanations[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Sanity-check-our-explanations)

To better make sense of the feature attributions we're getting, we should compare them with our model's baseline. In most cases, the sum of your attribution values + the baseline should be very close to your model's predicted value for each input. Also note that for regression models, the `baseline_score` returned from AI Explanations will be the same for each example sent to your model. For classification models, each class will have its own baseline.

In this section we'll send 10 test examples to our model for prediction in order to compare the feature attributions with the baseline. Then we'll run each test example's attributions through two sanity checks in the `sanity_check_explanations` method.

In [0]:

*# Prepare 10 test examples to our model for prediction*for  i  in  range(10):  with  open('bike-data-10.txt',  'a')  as  outfile:  json.dump({'dense_input':  test_data.iloc[i].values.tolist()},  outfile)  outfile.write('\n')

In [0]:

*# Make the request with gcloud*batch_explain  =  !gcloud  beta  ai-platform  explain  --model  $MODEL  --version  $VERSION  --json-instances='bike-data-10.txt'attributions_resp  =  json.loads(batch_explain.s)

In the function below we perform two sanity checks for models using Integrated Gradient (IG) explanations and one sanity check for models using Sampled Shapley.

In [0]:

def  sanity_check_explanations(example,  mean_tgt_value=None,  variance_tgt_value=None):  passed_test  =  0  total_test  =  1  *# `attributions` is a dict where keys are the feature names*  *# and values are the feature attributions for each feature*  attribution_vals  =  [x[0]  for  x  in  example['attributions_by_label'][0]['attributions'].values()]  baseline_score  =  example['attributions_by_label'][0]['baseline_score']  sum_with_baseline  =  np.sum(attribution_vals)  +  baseline_score  predicted_val  =  example['attributions_by_label'][0]['example_score']  *# Sanity check 1 *  *# The prediction at the input is equal to that at the baseline.*  *# Please use a different baseline. Some suggestions are: random input, training*  *# set mean.*  if  abs(predicted_val  -  baseline_score)  <=  0.05:  print('Warning: example score and baseline score are too close.')  print('You might not get attributions.')  else:  passed_test  +=  1  *# Sanity check 2 (only for models using Integrated Gradient explanations)*  *# Ideally, the sum of the integrated gradients must be equal to the difference*  *# in the prediction probability at the input and baseline. Any discrepency in*  *# these two values is due to the errors in approximating the integral.*  if  explain_method  ==  'integrated-gradients':  total_test  +=  1  want_integral  =  predicted_val  -  baseline_score  got_integral  =  sum(attribution_vals)  if  abs(want_integral-got_integral)/abs(want_integral)  >  0.05:  print('Warning: Integral approximation error exceeds 5%.')  print('Please try increasing the number of integrated gradient steps.')  else:  passed_test  +=  1  print(passed_test,  ' out of ',  total_test,  ' sanity checks passed.')

In [0]:

for  i  in  attributions_resp['explanations']:  sanity_check_explanations(i)

## Understanding AI Explanations with the What-If Tool[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Understanding-AI-Explanations-with-the-What-If-Tool)

In this section we'll use the [What-If Tool](https://pair-code.github.io/what-if-tool/) to better understand how our model is making predictions. See the cell below the What-if Tool for visualization ideas.

The What-If-Tool expects data with keys for each feature name, but our model expects a flat list. The functions below convert data to the format required by the What-If Tool.

In [0]:

*# This is the number of data points we'll send to the What-if Tool*WHAT_IF_TOOL_SIZE  =  500from  witwidget.notebook.visualization  import  WitWidget,  WitConfigBuilderdef  create_list(ex_dict):  new_list  =  []  for  i  in  feature_names:  new_list.append(ex_dict[i])  return  new_listdef  example_dict_to_input(example_dict):  return  {  'dense_input':  create_list(example_dict)  }from  collections  import  OrderedDictwit_data  =  test_data.iloc[:WHAT_IF_TOOL_SIZE].copy()wit_data['duration']  =  test_labels[:WHAT_IF_TOOL_SIZE]wit_data_dict  =  wit_data.to_dict(orient='records',  into=OrderedDict)

In [0]:

config_builder  =  WitConfigBuilder(  wit_data_dict  ).set_ai_platform_model(  PROJECT_ID,  MODEL,  VERSION,  adjust_example=example_dict_to_input  ).set_target_feature('duration').set_model_type('regression')WitWidget(config_builder)

### What-If Tool visualization ideas[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#What-If-Tool-visualization-ideas)

On the x-axis, you'll see the predicted trip duration for the test inputs you passed to the What-If Tool. Each circle represents one of your test examples. If you click on a circle, you'll be able to see the feature values for that example along with the attribution values for each feature.

- You can edit individual feature values and re-run prediction directly within the What-If Tool. Try changing `distance`, click **Run inference** and see how that affects the model's prediction
- You can sort features for an individual example by their attribution value, try changing the sort from the attributions dropdown
- The What-If Tool also lets you create custom visualizations. You can do this by changing the values in the dropdown menus above the scatter plot visualization. For example, you can sort data points by inference error, or by their similarity to a single datapoint.

## Cleaning up[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#Cleaning-up)

To clean up all GCP resources used in this project, you can [delete the GCP project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) you used for the tutorial.

Alternatively, you can clean up individual resources by running the following commands:

In [0]:

*# Delete model version resource*!gcloud  ai-platform  versions  delete  $VERSION  --quiet  --model  $MODEL*# Delete model resource*!gcloud  ai-platform  models  delete  $MODEL  --quiet*# Delete Cloud Storage objects that were created*!gsutil  -m  rm  -r  $BUCKET_NAME

If your Cloud Storage bucket doesn't contain any other objects and you would like to delete it, run `gsutil rm -r gs://$BUCKET_NAME`.

## What's next?[¶](https://render.githubusercontent.com/view/ipynb?commit=b4b36f9ee8ad8f3a610a8d8e6367006ee6cff02f&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f476f6f676c65436c6f7564506c6174666f726d2f6d6c2d6f6e2d6763702f623462333666396565386164386633613631306138643865363336373030366565366366663032662f7475746f7269616c732f6578706c616e6174696f6e732f61692d6578706c616e6174696f6e732d746162756c61722e6970796e62&nwo=GoogleCloudPlatform%2Fml-on-gcp&path=tutorials%2Fexplanations%2Fai-explanations-tabular.ipynb&repository_id=100992520&repository_type=Repository#What's-next?)

To learn more about AI Explanations or the What-if Tool, check out the resources here.

- [AI Explanations documentation](https://render.githubusercontent.com/view/cloud.google.com/ml-engine/docs/ai-explanations)
- [Documentation for using the What-if Tool with Cloud AI Platform models](https://cloud.google.com/ml-engine/docs/using-what-if-tool)
- [What-If Tool documentation and demos](https://pair-code.github.io/what-if-tool/)
- [Integrated gradients paper](https://arxiv.org/abs/1703.01365)

- © 2020 GitHub, Inc.

- [Terms](https://github.com/site/terms)

- [Privacy](https://github.com/site/privacy)

- [Security](https://github.com/security)

- [Status](https://githubstatus.com/)

- [Help](https://help.github.com/)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' height='24' class='octicon octicon-mark-github js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='24' aria-hidden='true' data-evernote-id='46'%3e%3cpath fill-rule='evenodd' d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z' data-evernote-id='640' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/)

- [Contact GitHub](https://github.com/contact)

- [Pricing](https://github.com/pricing)

- [API](https://developer.github.com/)

- [Training](https://training.github.com/)

- [Blog](https://github.blog/)

- [About](https://github.com/about)