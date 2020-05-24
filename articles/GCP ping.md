GCP ping

# Measure your latency to [GCP regions](https://cloud.google.com/compute/docs/regions-zones/regions-zones)

| REGION | MEDIAN LATENCY |
| --- | --- |
| Tokyo<br>asia-northeast1 | 228ms |
| Osaka<br>asia-northeast2 | 238ms |
| Hong Kong<br>asia-east2 | 271ms |
| Singapore<br>asia-southeast1 | 305ms |
| Mumbai<br>asia-south1 | 367ms |
| Taiwan<br>asia-east1 | 28840ms |

[![](../_resources/9e18b2ef3784685fc2135b36a57abd10.png)](https://twitter.com/share?text=My%20lowest-latency%20%23GCP%20regions%20via%20gcping.com%3A%0Aasia-northeast1%20(228ms)%0Aasia-northeast2%20(238ms)%0Aasia-east2%20(271ms))

## How does this work?

Your browser makes HTTP requests to `f1-micro` instances in each region. The median time between request and response is shown.

The **global** row uses a [Global HTTP Load Balancer](https://cloud.google.com/load-balancing/) to route requests to the nearest healthy instance.

This is not an official Google project. [Source available on GitHub](https://github.com/imjasonh/gcping).