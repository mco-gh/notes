Protecting our Google Cloud customers from new vulnerabilities without impacting performance

# Protecting our Google Cloud customers from new vulnerabilities without impacting performance

Ben Treynor Sloss

VP, 24x7

If you’ve been keeping up on the latest tech news, you’ve undoubtedly heard about the CPU security flaw that [Google’s Project Zero disclosed](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html) last Wednesday. On Friday, [we answered some of your questions](https://blog.google/topics/google-cloud/answering-your-questions-about-meltdown-and-spectre/) and detailed how we are protecting Cloud customers. Today, we’d like to go into even more detail on how we’ve protected Google Cloud products against these speculative execution vulnerabilities, and what we did to make sure our Google Cloud customers saw minimal performance impact from these mitigations.

Modern CPUs and operating systems protect programs and users by putting a “wall" around them so that one application, or user, can’t read what’s stored in another application’s memory. These boundaries are enforced by the CPU.

But as we disclosed last week, Project Zero discovered techniques that can circumvent these protections in some cases, allowing one application to read the private memory of another, potentially exposing sensitive information.

The vulnerabilities come in three variants, each of which must be protected against individually. Variant 1 and Variant 2 have also been referred to as “Spectre.” Variant 3 has been referred to as “Meltdown.” Project Zero [described these in technical detail](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html), the [Google Security blog](https://security.googleblog.com/) described how we’re [protecting users across all Google products](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-need.html), and we explained how we’re protecting Google Cloud customers and [provided guidance on security best practices for customers who use their own operating systems](https://blog.google/topics/google-cloud/answering-your-questions-about-meltdown-and-spectre/) with Google Cloud services.

Surprisingly, these vulnerabilities have been present in most computers for nearly 20 years. Because the vulnerabilities exploit features that are foundational to most modern CPUs—and were previously believed to be secure—they weren’t just hard to find, they were even harder to fix. For months, hundreds of engineers across Google and other companies worked continuously to understand these new vulnerabilities and find mitigations for them.

In September, we began deploying solutions for both Variants 1 and 3 to the production infrastructure that underpins all Google products—from Cloud services to Gmail, Search and Drive—and more-refined solutions in October. Thanks to extensive performance tuning work, these protections caused no perceptible impact in our cloud and required no customer downtime in part due to Google Cloud Platform’s Live Migration technology. No GCP customer or internal team has reported any performance degradation.

While those solutions addressed Variants 1 and 3, it was clear from the outset that Variant 2 was going to be much harder to mitigate. For several months, it appeared that disabling the vulnerable CPU features would be the only option for protecting all our workloads against Variant 2. While that was certain to work, it would also disable key performance-boosting CPU features, thus slowing down applications considerably.

Not only did we see considerable slowdowns for many applications, we also noticed inconsistent performance, since the speed of one application could be impacted by the behavior of other applications running on the same core. Rolling out these mitigations would have negatively impacted many customers.

With the performance characteristics uncertain, we started looking for a “moonshot”—a way to mitigate Variant 2 without hardware support. Finally, inspiration struck in the form of “[Retpoline](https://support.google.com/faqs/answer/7625886)”—a novel software binary modification technique that prevents branch-target-injection, created by Paul Turner, a software engineer who is part of our Technical Infrastructure group. With Retpoline, we didn't need to disable speculative execution or other hardware features. Instead, this solution modifies programs to ensure that execution cannot be influenced by an attacker.

With Retpoline, we could protect our infrastructure at compile-time, with no source-code modifications. Furthermore, testing this feature, particularly when combined with optimizations such as software branch prediction hints, demonstrated that this protection came with almost no performance loss.

We immediately began deploying this solution across our infrastructure. In addition to sharing the technique with industry partners upon its creation, we [open-sourced](https://support.google.com/faqs/answer/7625886) our compiler implementation in the interest of protecting all users.

By December, all Google Cloud Platform (GCP) services had protections in place for all known variants of the vulnerability. During the entire update process, nobody noticed: we received no customer support tickets related to the updates. This confirmed our internal assessment that in real-world use, the performance-optimized updates Google deployed do not have a material effect on workloads.

We believe that Retpoline-based protection is the best-performing solution for Variant 2 on current hardware. Retpoline fully protects against Variant 2 without impacting customer performance on all of our platforms. In sharing our research publicly, we hope that this can be universally deployed to improve the cloud experience industry-wide.

This set of vulnerabilities was perhaps the most challenging and hardest to fix in a decade, requiring changes to many layers of the software stack. It also required broad industry collaboration since the scope of the vulnerabilities was so widespread. Because of the extreme circumstances of extensive impact and the complexity involved in developing fixes, the response to this issue has been one of the few times that Project Zero made [an exception to its 90-day disclosure policy](https://security.googleblog.com/2015/02/feedback-and-data-driven-updates-to.html).

While these vulnerabilities represent a new class of attack, they're just a few among the many different types of threats our infrastructure is designed to defend against every day. Our infrastructure includes [mitigations by design and defense-in-depth](https://www.google.com/cloud/security/infrastructure/), and we’re committed to ongoing research and contributions to the security community and to protecting our customers as new vulnerabilities are discovered.