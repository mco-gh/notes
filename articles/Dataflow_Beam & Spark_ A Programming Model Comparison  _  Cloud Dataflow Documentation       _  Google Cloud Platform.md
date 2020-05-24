Dataflow/Beam & Spark: A Programming Model Comparison  |  Cloud Dataflow Documentation       |  Google Cloud Platform

star_border
star_border
star_border
star_border
star_border

- [Cloud Dataflow](https://cloud.google.com/dataflow/)

- chevron_right

 [Documentation](https://cloud.google.com/dataflow/docs/)

#  Dataflow/Beam & Spark: A Programming Model Comparison

- [Contents](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#top_of_page)
- [Logistics](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#logistics)
- [User Scores: Classic batch processing](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#user-scores-classic-batch-processing)
- [Hourly Team Scores: Windowing](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#hourly-team-scores-windowing)
- [Leaderboard: Robust stream processing](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#leaderboard-robust-stream-processing)
- [Game Stats: Advanced stream processing](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#game-stats-advanced-stream-processing)
- [Conclusion](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#conclusion)

By Tyler Akidau & Frances Perry, Software Engineers, Apache Beam Committers
Code examples by: Amy Unruh, Paul Newson, & Jerry Zhao, Software Engineers

[@takidau](https://twitter.com/takidau), [@francesjperry](https://twitter.com/francesjperry), [@amygdala](https://twitter.com/amygdala), [@newsons_nybbles](https://twitter.com/newsons_nybbles)

February 3, 2016

**NOTE (August 19, 2016): This comparison highlights differences in the programming models of Cloud Dataflow/Apache Beam and Apache Spark 1.x. Many of the Beam model concepts highlighted in this post are now being incorporated into Spark 2.0 and later releases.**

With the programming model/SDK portion of [Google Cloud Dataflow](https://cloud.google.com/dataflow/) moving into an Apache Software Foundation incubator project, [Apache Beam](http://incubator.apache.org/projects/beam.html), we thought now a good time to discuss the unique features and capabilities that distinguish Dataflow from [Apache Spark](http://spark.apache.org/), from a strictly programming-model perspective.

Dataflow is unique amongst data parallel systems in that it is built upon a comprehensive model for out-of-order processing: one designed to meet the challenges of real-time data processing without compromising correctness, motivated by our years of experience with production batch and streaming systems at Google. We've written at length about the importance of the semantics enabled by features such as event-time windowing, watermarks, and triggers. The World Beyond Batch: [Streaming 101](http://oreilly.com/ideas/the-world-beyond-batch-streaming-101) and [Streaming 102](http://oreilly.com/ideas/the-world-beyond-batch-streaming-102) posts on O'Reilly's Radar site and the VLDB 2015 paper on [The Dataflow Model](http://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf) are good places to start. Though we'll continue to touch upon those points, much of this post will focus upon the practical elegance of the model, and how that directly translates into significant concrete benefits at the code level.

To highlight the distinguishing features of the Dataflow model, we'll be comparing code side-by-side with Spark code snippets. Spark has had a large and positive impact on the industry thanks to doing a number of things much better than other systems had done before. But Dataflow holds distinct advantages in programming model flexibility, power, and expressiveness, particularly in the out-of-order processing and real-time session management arenas.

No other massive-scale data parallel programming model provides the depth-of-capability and ease-of-use that Dataflow/Beam does.

Your code, too, will benefit from moving onto models specifically created for the out-of-order data-processing needs of today, based off of real-world experience with massive-scale use cases, and designed with an eye towards marrying clarity and simplicity with expressiveness and flexibility. The fact is: no other massive-scale data parallel programming model provides the depth-of-capability and ease-of-use that Dataflow/Beam does. We hope to showcase a little bit of that magic in this post.

### Logistics

Let's start with logistics. This post will explore four data-processing use cases for a mobile gaming scenario: mobile users play games on their phones, game scores are uploaded to backend servers, and various analyses are then performed on those scores:

1. **User Scores** - A classic batch pipeline calculating per-user scores over a bounded set of input data.

2. **Hourly Team Scores** - A batch pipeline calculating per-hour, per-team scores over a bounded set of input data.

3. **Leaderboard** - A streaming pipeline continuously calculating two types of scores: per-hour, per-team scores as before, and cumulative per-user score totals over all time.

4. **Game Stats** - A streaming pipeline computing spam-filtered, per-hour, per-team scores, as well as a more complex hourly analysis of average per-user engagement time for the game.

For those of you who want to see the raw code, it's available on GitHub for both [Dataflow](https://github.com/GoogleCloudPlatform/DataflowSDK-examples/tree/master-1.x/src/main/java8/com/google/cloud/dataflow/examples/complete/game) and [Spark](https://github.com/GoogleCloudPlatform/spark-examples/tree/master/gaming/java). But rather than try to walk you through all of the code step-by-step (the Dataflow side of which is already covered quite well by our [Mobile Gaming Pipeline Examples](https://cloud.google.com/dataflow/examples/gaming-example) walkthrough), our focus here will be on showing you why the Dataflow model much more elegantly addresses the real-world needs of batch and streaming pipeline builders.

To do so, we're going to frame our points within the context of the four critical questions all data processing practitioners must attempt to answer when building their pipelines:

- ***What* results are calculated?** Sums, joins, histograms, machine learning models?
- ***Where* in event time are results calculated?** Does the time each event originally occurred affect results? Are results aggregated in fixed windows, sessions, or a single global window?
- ***When* in processing time are results materialized?** Does the time each event is observed within the system affect results? When are results emitted? Speculatively, as data evolve? When data arrive late and results must be revised? Some combination of these?
- ***How* do refinements of results relate?** If additional data arrive and results change, are they independent and distinct, do they build upon one another, etc.?

These questions provide a nice framework for thinking about data parallel problems, and the dimensions along which they are split were informed by years of experience spent observing the ways in which pipelines evolve and change over time. It's very common to want to change the answer for one question while leaving the answers for the others untouched; having a model which is partitioned along these lines leads to code which is easier to evolve and maintain, as we'll see below.

If these colorful questions don't look familiar to you, or if you need a refresher on core out-of-order processing concepts like event time vs. processing time, windowing, watermarks, and triggers, it would be well worth your time to read through Tyler's World Beyond Batch posts on O'Reilly's Radar site before tackling this one. They're big, but worth the investment.

- [The World Beyond Batch: Streaming 101](http://oreilly.com/ideas/the-world-beyond-batch-streaming-101)
- [The World Beyond Batch: Streaming 102](http://oreilly.com/ideas/the-world-beyond-batch-streaming-102)

Lastly, note that we'll be using Java in all the code examples in this post, for consistency of comparison. Scala pundits would be right in pointing out that the amount of code necessary with Spark's Scala API would be notably smaller. However, the same argument would apply to a Scala Dataflow API (a nascent open-source version of which already exists, and which seems likely to flower into maturity in due time given Dataflow's move to join the ASF). Furthermore, as we'll see below, code size will be of secondary importance to clarity and modularity as our pipelines evolve. We'll thus consider the Scala argument moot for the sake of this comparison.

### User Scores: Classic batch processing

To begin with, consider a very simple pipeline which simply calculates per-user score totals over a bounded set of input data. A pipeline like this could be used to calculate the total cumulative scores racked up by each user of a given game over all time. Each time you wanted to update the per-user totals, you would simply re-execute the pipeline over the logs for the desired time period.

A simple batch pipeline such as this one only explicitly addresses the first question in the quadrumvirate. For the other three, it takes the defaults that have long been provided by all batch processing systems:

|     |     |
| --- | --- |
| What? | Sums of integers, keyed by user. |
| Where? | Within a single, implicit, global event-time window (i.e., event time is ignored). |
| When? | Once, when the entire bounded input source has been consumed. |
| How? | Irrelevant, since only one output is produced per window. |

Table 1: What/Where/When/How answers for the User Scores pipeline.

As one might expect for such a simple pipeline, the core logic for the two versions of the code is quite similar:

| Dataflow | Spark |
| --- | --- |
| ━ Sum<br>gameEvents [... input ...] [... filter ...] .apply("ExtractUserScore", new ExtractAndSumScore("user")) [... output ...]; | ┓ ┻ Sum<br>gameEvents [... input ...] [... filter ...] .mapToPair(new ExtractUserScore()) .reduceByKey(new SumScore()) [... output ...]; |

Listing 1: User Scores - a simple pipeline to compute per-user scores. [[Dataflow code](https://github.com/GoogleCloudPlatform/DataflowSDK-examples/blob/master-1.x/src/main/java8/com/google/cloud/dataflow/examples/complete/game/UserScore.java#L229), [Spark code](https://github.com/GoogleCloudPlatform/spark-examples/blob/master/gaming/java/src/main/java/com/google/cloud/sparkdemo/UserScore.java#L227)]

One minor difference worth noting up front: our `ExtractAndSumScore` transform does exactly the same thing as the corresponding two lines on the right for Spark; we just have it collapsed into a single composite transform here, because the Dataflow model is flexible enough that we'll be able to reuse it across the other pipelines below.

Though we'll touch upon a few more minor differences later on, the point of this first pipeline is mostly to establish a baseline for comparison with a scenario that's essentially equivalent between the two technologies. So for now, let's move on.

### Hourly Team Scores: Windowing

To make things a little more interesting, our next example will calculate per-team scores, bucketed into one-hour fixed windows. You could imagine this being useful for long-running tournaments engaged in by teams scattered across the globe, where specific prizes are awarded to teams with the highest scores for any given hour of the day.

Even though we're still only dealing with bounded data, we now need to directly address two of the four questions:

|     |     |
| --- | --- |
| What? | Sums of integers, keyed by team. |
| Where? | Within fixed event-time windows of one hour. |
| When? | Once, when the entire bounded input source has been consumed. |
| How? | Irrelevant, since only one output is produced per window. |

Table 2: What/Where/When/How answers for the Hourly Team Scores pipeline.

The beauty of the Dataflow model is that the addition of code to change our answer for the "*Where?*" question requires zero changes in the code that addresses the "*What?*" question; we simply add two statements: one to assign timestamps to records (since the bounded `TextIO` source we're using doesn't know how to extract them from the records themselves), and another to assign a windowing strategy. Bam! Done.

The Spark model, on the other hand, lacking a formal notion of event-time windowing, requires us to intermingle the "*What?*" and "*Where?*" portions of the code, by introducing a representation of the current window into the data themselves as a secondary portion of the key. This becomes quite apparent when looking at the code in question, where instead of distinct blue and yellow blocks as we had in Dataflow, we now have a mix of the two colors across the entire pipeline (note that we're eliding portions of the pipeline, such as input and filtering, that are essentially identical and don't contribute materially to the comparison; also, apologies in advance for the width of the remaining code snippet listings, but seeing them side-by-side really is the best way to get a sense of comparison).

| Dataflow | Spark |
| --- | --- |
| ┓ ┣ Window┃ ┛ ━ Sum<br>gameEvents [... input ...] [... filter ...] .apply("AddEventTimestamps", WithTimestamps.of((GameActionInfo i) -> new Instant(i.getTimestamp()))) .apply("FixedWindowsTeam", Window.<GameActionInfo>into( FixedWindows.of(Duration.standardMinutes(windowDuration)))) .apply("ExtractTeamScore", new ExtractAndSumScore("team")) [... output ...]; | ┓ ┃ ┣ Window┃ & Sum┛<br>gameEvents [... input ...] [... filter ...] .mapToPair(event -> new Tuple2<WithTimestamp<String>, Integer>( WithTimestamp.create(event.getTeam(), (event.getTimestamp() / windowDuration) * windowDuration), event.getScore())) .reduceByKey(new SumScore()); [... output ...]; |

Listing 2: Hourly Team Scores - a pipeline to compute per-team scores, grouped into hourly event-time windows. [[Dataflow code](https://github.com/GoogleCloudPlatform/DataflowSDK-examples/blob/master-1.x/src/main/java8/com/google/cloud/dataflow/examples/complete/game/HourlyTeamScore.java#L175), [Spark code](https://github.com/GoogleCloudPlatform/spark-examples/blob/master/gaming/java/src/main/java/com/google/cloud/sparkdemo/HourlyTeamScore.java#L156)]

So while the actual amount of code involved at this point is still quite similar, you can see that the two concepts (*what* we're computing, and *where* in event time) have already become quite conflated with Spark. And this is a fairly minimal example. That sort of intertwining translates into a compounding of code complexity down the line as the pipeline evolves into something more sophisticated, examples of which we'll see below.

### Leaderboard: Robust stream processing

We'll first discuss briefly what it would take to migrate the previous batch pipeline directly to streaming mode. After that, we'll look at what it takes to combine the first two pipelines together into a streaming pipeline that also provides low-latency, eventually-correct results.

#### Batch to Streaming

Though migrating the batch pipeline in [Listing 2](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#Listing2) to run in streaming mode would be relatively straightforward in both systems (update I/O sources/sinks to streaming equivalents, additionally update data types from RDDs to DStreams for Spark), the streaming versions would yield vastly different results in the two models:

- With Dataflow, the nature of results would remain essentially consistent: for any given team, you would continue to receive a single output per team and hourly event-time window, just now in a streaming fashion, as the watermark (the system's notion of progress in the event-time domain; see [Streaming 101](http://oreilly.com/ideas/the-world-beyond-batch-streaming-101) and [102](http://oreilly.com/ideas/the-world-beyond-batch-streaming-102) for more details) passes the end of the window.
- With Spark, the nature of results would change: you'd now get one output per team, per hourly event-time window, per micro-batch (for every micro-batch that observed input for a given team). You'd then need to write additional code to sum up those per micro-batch scores and arrive at a single per-team per-hour result (which is exactly what we'll be doing in the next pipeline).

This is an example of Spark's underlying architecture bleeding through into the model and observed results; we'll see more of that below. For now, suffice it to say that the Dataflow model provides a more semantically consistent experience when performing a straightforward batch to streaming conversion.

#### Robust Streaming

Now, for our third pipeline, we're going to up the ante in two dimensions. Firstly, we'll combine the concepts from the previous two pipelines, calculating two different sets of scores in tandem: hourly team scores (which will window in the event time domain) and all-time user score totals (which will "window" in the processing-time domain). Secondly, we'll also add support for low-latency updates to our outputs as the input evolves, since that's one of the main allures of streaming.

At the same time, we need to maintain the standards of quality established in the first two pipelines, principally that we continue to eventually provide the correct answer, in addition to the speculative, low-latency answers that will give our data a sense of freshness as time progresses. If we stop providing accurate score tallies, we will quickly experience the wrath of our game-playing customers. And one can only imagine the horrors we would incur if we were instead processing financial transactions.

##### Hourly Team Scores

The hourly team scores portion is perhaps the more interesting of the two, because it focuses on event-time windowing, which is a much trickier beast in streaming mode. To achieve our goal of low-latency, eventually correct results, we're now forced to explicitly answer the final two questions:

- *When* in processing time are results materialized?
- *How* do refinements of results relate?

*When* you materialize results depends a lot upon how often you need to see them; *how* the various refinements relate typically depends a lot upon how they're being utilized outside of the pipeline.

In the *when* case, there are commonly four facets to the answer, all of which revolve around some notion of input completeness in the event-time domain (which in Dataflow is provided by watermarks). Tyler goes into completeness metrics and watermarks in much more detail in [Streaming 102](http://oreilly.com/ideas/the-world-beyond-batch-streaming-102), but the basic milestones for results in a window are, in order:

1. **Early:** Providing early, speculative results before the window is complete to show the answer evolving over time.

2. **On-time:** Knowing or estimating when the input data are complete for a given event time window.

3. **Late:** In the case where our notion of completeness is an estimate (e.g., when mobile devices are involved, due to their tendency to go offline for long periods of time and later upload events from the past when they come back online), providing updated results to account for data that arrive late relative to our heuristic notion of completeness.

4. **Final:** Declaring when we are completely done with a given window, so that a final result can be provided (and the associated persistent state garbage collected, since accumulating state for all the inputs we've ever seen is typically impractical given physical and fiscal limitations).

Not all use cases care about observing the contents of windows multiple times as they evolve. But for those that do, we refer to each materialization of a window as a *pane*. And as we'll see below, we use *triggers* in the code to declare the points in time when we want to see those panes materialized, with watermarks used to delineate levels of input completeness, as described above.

For our use case, where we're dealing with one-hour windows, we'd like to provide timely updates until the input for the window becomes complete, an updated answer upon achieving completeness, perhaps slightly less timely results for revisions due to late data, and then a final answer for the window after we've processed two additional hours' worth of data. This essentially means that anyone playing a game has to report their scores within two hours of completing a game for their scores to be counted in the tally, which is something that can be documented clearly in the rules for the tournament so users understand what their playing field looks like.

In the *how* case, we want to be able to write a new version of the given score every time it's updated. As such, each output pane will need to include all of the accumulated values observed thus far.

Given all that, the desired answers to our four questions for the hourly team scores portion of this pipeline will look something like the following:

|     |     |
| --- | --- |
| What? | Sums of integers, keyed by team. |
| Where? | Within fixed event-time windows of one hour. |
| When? | - **Early:** Every 5 minutes of processing time.<br>- **On-time:** When the watermark passes the end of the window.<br>- **Late:** Every 10 minutes of processing time.<br>- **Final:** When the watermark passes the end of the window + two hours. |
| How? | Panes accumulate new values into prior results. |

Table 3: What/Where/When/How answers for the per-team, per-hour portion of the Leaderboard pipeline.

In Dataflow, the answers to these four questions again map nicely onto four independent sections of code. This provides clarity of intent, and also makes it easy to swap in different answers to each of the different questions depending upon your use case.

With Spark, the lack of event-time windowing support requires us to emulate as many of these features as possible using the available APIs, resulting in additional code, duplicated logic, and pieces of the four answers scattered across the entire codebase.

| Dataflow | Spark |
| --- | --- |
| ┓ ┣ Window┛ ━ Watermark Trigger┳ Early Trigger┛ ┳ Late Trigger┛ ━ Garbage Collection━ Accumulation━ Sum<br>gameEvents [... input ...] .apply("LeaderboardTeamFixedWindows", Window .<GameActionInfo>into(FixedWindows.of( Duration.standardMinutes(Durations.minutes(60))))  .triggering(AfterWatermark.pastEndOfWindow() .withEarlyFirings(AfterProcessingTime.pastFirstElementInPane() .plusDelayOf(Durations.minutes(5))) .withLateFirings(AfterProcessingTime.pastFirstElementInPane() .plusDelayOf(Durations.minutes(10)))) .withAllowedLateness(Duration.standardMinutes(120)  .accumulatingFiredPanes()) .apply("ExtractTeamScore", new ExtractAndSumScore("team")) [... output ...] | ┓ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ Window,┃ Trigger,┃ Garbage┃ Collection,┣ Accumulation,┃ & Sum (with┃ no Watermark)┃ all mixed┃ together.┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┛<br>final Long allowedLatenessMs = Durations.minutes(120).milliseconds(); final Long teamWindowDurationMs = Durations.minutes(60).milliseconds();<br>gameEvents [... input ...] .filter(gInfo -> gInfo.getTimestamp() > System.currentTimeMillis() - allowedLatenessMs - teamWindowDurationMs) .mapToPair(gInfo -> new Tuple2<>(WithTimestamp.create( gInfo.getTeam(), (gInfo.getTimestamp() / teamWindowDurationMs) * teamWindowDurationMs), gInfo.getScore())) .reduceByKey(new SumScore()) .transformToPair((rdd, timestamp) -> { teamWindowTimestamp.set(Math.max( teamWindowTimestamp.get(), timestamp.milliseconds())); return rdd; }) .updateStateByKey(new  SumAggregator()  .setTTL(allowedLatenessMs + teamWindowDurationMs)); .filter(x -> x._2().timestamp() >= teamWindowTimestamp.get()) [... output ...]private static class SumAggregator implements Function2< List, Optional<WithTimestamp<Integer>>, Optional>> { final private static WithTimestamp<Integer> INITIAL_STATE = WithTimestamp.create(0, 0L); private Long TTL = Long.MAX_VALUE;<br>SumAggregator setTTL(Long TTL) { this.TTL = TTL; return this; } public Optional<WithTimestamp<Integer>> call( List scores, Optional<WithTimestamp<Integer>> state) { final Long cutoffTime = System.currentTimeMillis() - TTL; if (state.isPresent() && state.get().timestamp() < cutoffTime) { return Optional.absent(); } if (scores.size() == 0) return state; WithTimestamp<Integer> sumWithTimestamp = state.or(INITIAL_STATE); Integer sum = sumWithTimestamp.val() + scores.stream().mapToInt(Integer::intValue).sum(); return Optional.of(WithTimestamp.create( sum, System.currentTimeMillis())); } } |

Listing 3: The hourly team scores portion of the Leaderboard pipeline. [[Dataflow code](https://github.com/GoogleCloudPlatform/DataflowSDK-examples/blob/master-1.x/src/main/java8/com/google/cloud/dataflow/examples/complete/game/LeaderBoard.java#L191), [Spark code](https://github.com/GoogleCloudPlatform/spark-examples/blob/master/gaming/java/src/main/java/com/google/cloud/sparkdemo/LeaderBoard.java#L234)]

There are two benefits we want to specifically call out for Dataflow: clarity/modularity of code, and semantic correctness.

###### Clarity & Modularity

Because the Dataflow model is designed to allow answers for the four questions to change independently, the pipeline evolves cleanly as we shape our outputs in ever more sophisticated ways (e.g., providing low-latency, speculative results, while still maintaining correctness). On the flipside, when answers for the various questions are commingled, it becomes much more difficult to extract the logic for a specific answer into a reusable module.

This is the difference between a unified batch and streaming **engine**, which Spark most definitely does have, and a unified batch and streaming **model and API**, which Spark most definitely lacks.

A concrete example of this is the way we've been able to reuse the same `ExtractAndSumScore` transform across all three Dataflow pipelines we've looked at so far. For Spark, we were stuck duplicating our simple summation logic in the `SumAggregator` as part of the transition to streaming, to both compensate for Spark's micro-batch architecture bleeding through into the semantic model, as well as cope with the function signature differences in the parameters required by `reduceByKey` and `updateStateByKey`/`mapWithState`. This is the difference between a unified batch and streaming *engine*, which Spark most definitely does have, and a unified batch and streaming *model and API*, which Spark most definitely lacks.

###### Correctness

With respect to correctness, Dataflow remains resilient to operational disturbances (e.g., input delays) thanks to its utilization of the watermark as a notion of completeness. This is more easily understood within the context of an example.

Imagine we're running our two hourly-team-score pipelines, Dataflow and Spark. Both are providing low-latency, speculative results by keeping per-hour, per-team sums in some form of persistent state. From a correctness perspective, the two are essentially identical up to this point.

Hope is a decidedly unsound strategy when dealing with correctness in distributed systems.

However, in most use cases, it's impractical to keep state for all windows around indefinitely; physical and monetary limitations typically dictate a useful practical lifetime for windows, after which it's better to garbage collect them. In Dataflow, the lifetime of windows is bound by the progression of the watermark: after the watermark proceeds past some user-specified horizon beyond the end of a window, a final result for that window is produced, and the state for it garbage collected. In Spark, where no analog of watermarks exists to provide a notion of input completeness in the event-time domain, we're forced to just pick some point in processing time as the our line in the sand and hope for the best. But hope is a decidedly unsound strategy when dealing with correctness in distributed systems.

When inputs arrive in a reasonably timely manner, we may observe both strategies operating more or less equivalently. But if inputs become delayed for some reason, and the watermark is able to capture that fact (something which is quite often possible to design into watermark establishment algorithms), then the Dataflow pipeline will continue to provide correct answers in light of input delays (in addition to incremental results, as available), while the Spark pipeline will forge ahead, declaring windows complete and then closed well before they should be, resulting in incorrect results when the data eventually arrive and are dropped on account of exceeding the processing-time lateness horizon.

So in addition to increased clarity and reusability of code, there are semantic advantages to the Dataflow approach that directly affect correctness in light of the all-too-common operational disturbances we all encounter when dealing with distributed systems.

##### All-time User Scores

Having looked at the event-time fork of this pipeline, let's now look at the other half, which is computing global user-score sums over all time, with periodic updates in processing time. Since we're operating primarily in the processing-time domain here, one might think Dataflow brings less of a natural advantage than before, but it still yields benefits in the code clarity and modularity department, as we'll see below. But first, let's assess the semantics for this section of the pipeline.

This half of the pipeline computes total scores per-user, over all time, updated once every ten minutes. Event times are essentially irrelevant to this calculation, so we can effectively ignore the "*Where?*" question and take the default answer of using a single, global event-time window. As before, we simply want to write a new total score every time we have an update (i.e., updates to scores should accumulate over time), so we'll use the same accumulation mode as in the other half of the pipeline. As a result, our four answers for this part of the pipeline look something like this:

|     |     |
| --- | --- |
| What? | Sums of integers, keyed by user. |
| Where? | Within a single, implicit, global event-time window (i.e., event time is ignored). |
| When? | Every 10 minutes of processing-time. |
| How? | Panes accumulate new values into prior results. |

Table 4: What/Where/When/How answers for the per-user portion of the Leaderboard pipeline.

Before even looking at code, one thing worth calling out: in Dataflow, the periodic updates are driven by triggers; in Spark, the updates are driven by the micro-batch size. While this works semantically, it's generally a bad idea to bind pipeline semantics to execution engine parameters: it reduces portability, and can become limiting when the same execution engine settings also affect scalability, resource consumption levels, etc. In this case, triggering frequency is now directly bounded by micro-batch size, limiting flexibility in output patterns.

Moving on to the code: things do look better for Spark than in previous examples; there's less intermingling of colors happening on the Spark side (while the Dataflow side, as before, has the various concepts nicely partitioned).

| Dataflow | Spark |
| --- | --- |
| ━ Window┓ ┣ Trigger┃ ┛ ━ Lateness━ Accumulation━ Sum<br>gameEvents [... input ...] .apply("LeaderboardUserGlobalWindow", Window.<GameActionInfo>into(new GlobalWindows())  .triggering( Repeatedly.forever( AfterProcessingTime.pastFirstElementInPane() .plusDelayOf(Durations.minutes(10)))) .withAllowedLateness(Duration.standardMinutes(120))  .accumulatingFiredPanes()) .apply("ExtractUserScore", new ExtractAndSumScore("user")) [... output ...] | ┓ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ Window, Trigger┃ Accumulation,┣ & Sum (but no┃ Lateness), all┃ mixed together┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┛<br>gameEvents [... input ...] .window(Durations.minutes(10), Durations.minutes(10)) .mapToPair(new ExtractUserScore()) .reduceByKey(new SumScore()) .transformToPair((rdd, timestamp) -> { userWindowTimestamp.set(Math.max( userWindowTimestamp.get(), timestamp.milliseconds())); return rdd; }) .updateStateByKey(new  SumAggregator()) .filter(x -> x._2().timestamp() >= userWindowTimestamp.get()) [... output ...]private static class SumAggregator implements Function2< List, Optional, Optional> { final private static Integer INITIAL_STATE = 0;<br>public Optional call( List scores, Optional state) { if (scores.size() == 0) return state;<br>Integer sumWithTimestamp = state.or(INITIAL_STATE); Integer sum = sumWithTimestamp.val() + scores.stream().mapToInt(Integer::intValue).sum(); return Optional.of(sum); } } |

Listing 4: The global per-user scores portion of the Leaderboard pipeline. [[Dataflow code](https://github.com/GoogleCloudPlatform/DataflowSDK-examples/blob/master-1.x/src/main/java8/com/google/cloud/dataflow/examples/complete/game/LeaderBoard.java#L216), [Spark code](https://github.com/GoogleCloudPlatform/spark-examples/blob/master/gaming/java/src/main/java/com/google/cloud/sparkdemo/LeaderBoard.java#L279)]

As before in the hourly team scores section, we can reuse the same `ExtractAndSumScores` transformation we've used all along for Dataflow; for Spark, this time at least we can reuse the `SumAggregator` we wrote for the other half of this pipeline, thanks to the parameter that lets us choose the garbage collection horizon. But again, we've had to spread our otherwise-simple summation logic across two independent classes as part of the move to streaming, which is less than ideal. To make this clear, we've included a stripped-down version of the `SumAggregator` code here, with all the (unused) TTL code ripped out. Even with that functionality gone, the choice of accumulation still gets conflated with the choice of transformation (summation).

Lastly, even though we're mostly focusing on processing time in this section of the pipeline, it's still not possible to express the precise semantics our use case requires with Spark. To be 100% consistent with our policies in the hourly team scores portion of the pipeline, we should only treat scores as valid if they arrive in the pipeline before it processes two hours worth of additional data (in event time) past the end of the window they belong in. But having a consistent scoring policy like this requires the use of event time and a notion of completeness, which Spark lacks good support for. So we fudge a bit and just include all scores on the Spark side.

All in all, once you move into the streaming realm, things start to get much more difficult to express cleanly in Spark. It has a unified engine, but it doesn't have a truly unified model and API. Nor does it have a model which is designed with clarity and modularity in mind when dealing with the full suite of issues that one must confront in the out-of-order processing domain. These issues and more have come through quite clearly in the examples above, and thus far we've only been computing trivial sums of integers. Let's now take it one step further, and try to add a couple of slightly less-trivial features to our repertoire: spam detection and session windowing.

### Game Stats: Advanced stream processing

For this final pipeline, we're adding two additional features:

- **Spam filtering:** Abuse detection is a common requirement for real-world pipelines. For this example, we use a relatively simplistic heuristic that calculates the average per-user score globally for either a window (Dataflow) or a micro-batch (Spark), and then filters out any users whose scores are some significant amount larger than this global-average baseline. Though certainly not the most sophisticated algorithm, it's at least a reasonable approximation of what a first-pass attempt at spam detection might look like.
- **User Behavior Analysis:** To get us out of the realm of straightforward data aggregation, and more squarely into the realm of practical data analysis, we add a separate fork in the pipeline which computes user activity sessions (e.g., a sequence of game plays, none of which occurred more than 5 minutes apart from the prior game play in the session), and then calculates a global average of the sessions lengths. This average is a decent proxy for user engagement in the game, and can be used to measure user satisfaction and interest in a particular game at a broad level.

Also note that we've removed the user scores portion of the pipeline, since we aren't evolving it any further with this example.

#### Spam Filtering

For spam filtering, we won't actually look at any code; the two implementations here are quite similar in their approach. The main thing we want to call out here is an issue of correctness. The baseline used in our spam filtering algorithm is the average score across all users of the pipeline. In Dataflow, that average score is per event-time window; in Spark, it's per processing-time window (i.e., per micro-batch). That means that the Dataflow baseline for spam detection accurately reflects events as they happened, whereas the Spark baseline reflects events as they arrived at the pipeline.

If you care about correctness in a system that also cares about time, you need to use event-time windowing.

When data are arriving at the pipeline perfectly ordered, this is fine. Unfortunately, that almost never happens; for most use cases involving distributed systems, inputs are essentially never perfectly ordered. And the disorder just gets worse when inputs become unhealthy. Imagine your input is delayed for some subset of users; say network issues across the Atlantic keep European scores from arriving for a couple hours. When those data finally do arrive, you're going to get a couple hours' worth of European scores showing up at the same time as a few minutes' worth of non-European scores. This is going to wreak havoc on our abuse detection algorithm, since we're now comparing the average scores for European users over a massive window of time against the average scores of non-European users for a much more modest window of time. As is so frequently the case, if you care about correctness in a system that also cares about time, you need to use event-time windowing.

(Note that the other option for Spark would be to try to emulate event-time windowing as we have above, but that would bring with it all the shortcoming in clarity, maintainability, and simplicity that we've already covered.)

#### User Behavior Analysis

The sessions addition to the pipeline is interesting for two reasons:

- Session windows themselves are an example of **dynamic, data-driven windowing**. Dynamic windows are based off features of the data themselves, and thus evolve over time as more data arrive. For the Dataflow version, this change is a simple one-line modification to the windowing strategy; the Spark version, on the other hand, can no longer play the window-as-secondary-key trick used for static, fixed windows above in Listings [2](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#Listing2) and [3](https://cloud.google.com/dataflow/blog/dataflow-beam-and-spark-comparison#Listing3), and must resort to something a bit more clever and involved, using `updateStateByKey`/`mapWithState`. As we'll see however, even this solution has its limitations relative to the Dataflow version.
- After we build up the sessions, we then **re-window into fixed windows**, to allow us to generate statistics about the sessions we observe within regular intervals of time. So this portion of the pipeline will let us see what it's like to change our windowing strategy mid-stream, as it were.

Since we have two different groupings within this bit of the pipeline, we'll have two sets of answers to the *What*/*Where*/*When*/*How* questions:

|     |
| --- |
| 1. Per-user session lengths |
| What? | Per-user sessions lengths in event time. |
| Where? | Within session windows with gap duration of five minutes. |
| When? | Once, when the watermark passes the end of the window. |
| How? | Irrelevant, since only one output is produced per window. |
| 2. Global session length average |
| What? | Average session length for all users. |
| Where? | Within fixed event-time windows of one hour. |
| When? | Once, when the watermark passes the end of the window. |
| How? | Irrelevant, since only one output is produced per window. |

Table 5: What/Where/When/How answers for the two different grouping/windowing stages in the user behavior analysis part of the pipeline.

When looking at the code, the story for this pipeline remains much the same as before. The Dataflow code is very nicely partitioned across the answers to our questions, and since we were fine with the default triggering and accumulation behavior of yielding a single output when the watermark passes the end of the window, we don't even need to write any code for those answers. As in previous examples, the Spark code remains a tangle of the three relevant answers, with transformation, windowing, and triggering logic mixed together and spread out across the various classes and method invocations. It's also quite a lot of code. And that's despite the fact that we've omitted the code for the `Session` class, since it at least is strictly dedicated to answering the "*Where?*" question, and thus would be reusable in other pipelines with different answers to the other questions.

| Dataflow | Spark |
| --- | --- |
| ┓ ┣ Session Window┃ ┛ ━ Session Length━ Fixed Window━ Average Length┓ ┃ ┃ ┃ ┣ Session Length┃ ┃ ┃ ┃ ┛Note: Trigger and Garbage Collection both driven by Watermark via implicit defaults.<br>gameEvents [... input ...] .apply("WindowIntoSessions", Window.<KV<String, Integer>>into( Sessions.withGapDuration(Duration.standardMinutes(5))) .withOutputTimeFn(OutputTimeFns.outputAtEndOfWindow())) .apply("BuildSessions", Combine.perKey(x -> 0)) .apply("UserSessionActivity", ParDo.of(new CalculateSessionLength())) .apply("WindowToExtractSessionMean", Window.<Integer>into(FixedWindows.of(Duration.standardMinutes(30)))) .apply(Mean.<Integer>globally().withoutDefaults()) [... output ...]class CalculateSessionLength extends DoFn<KV<String, Integer>, Integer> implements RequiresWindowAccess { @Override public void processElement(ProcessContext c) { IntervalWindow w = (IntervalWindow) c.window(); int duration = new Duration(w.start(), .end()) .toPeriod().toStandardMinutes().getMinutes(); c.output(duration); } } | ┓ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ Session Window,┃ Session Length,┃ Fixed Window,┃ Average Length,┣ Trigger, & Garbage┃ Collection (with┃ no Watermark)┃ all mixed┃ together.┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┛<br>final Duration userActivityWindow = Durations.standardMinutes(30); final Long allowedLatenessMs = Durations.standardMinutes(120).milliseconds();<br>gameEvents [... input ...] .window(userActivityWindow, userActivityWindow)) .mapToPair((GameActionInfo gInfo) -> new Tuple2<>( gInfo.getUser(), gInfo.getTimestamp())) .updateStateByKey(new SessionizeUserActivities() .setGap(Durations.minutes(5))  .setTTL(allowedLatenessMs + userActivityWindow.milliseconds())) .mapValues(sessions -> sessions.stream() .filter(s -> s.closed) .collect(Collectors.toList())); .flatMapToPair(new SessionDurationByWindow( userActivityWindow.milliseconds())) .reduceByKey((a, b) -> new Tuple2<Long, Integer>( a._1() + b._1(), a._2() + b._2())) .mapValues(v -> v._1().doubleValue() / v._2() / 60.0 / 1000.0); [... output ...]class SessionizeUserActivities implements Function2< List, Optional>, Optional>> { private Long sessionGap; private Long TTL;<br>SessionizeUserActivities setGap(Long sessionGap) { this.sessionGap = sessionGap; return this; } SessionizeUserActivities setTTL(Long TTL) { this.TTL = TTL; return this; }<br>private void closeIfExpired(Session session, long cutoffTime) { if (session.end <= cutoffTime) session.close(); } @Override public Optional> call( List timestamps, Optional> state) { List sessions = state.or(new ArrayList()) .stream() .filter(session -> !session.closed) .collect(Collectors.toList()); final Long cutoffTime = System.currentTimeMillis() - TTL;<br>for (Long ts : timestamps) { if (ts > cutoffTime) sessions.add(new Session(ts, ts)); } if (sessions.size() == 0) return Optional.absent();<br>List mergedSessions = new ArrayList<>(); sessions.sort((a, b) -> (a.end.compareTo(b.end))); Session current = sessions.get(0); for (Session next : sessions.subList(1, sessions.size())) { if (next.start < current.end + sessionGap) { current.merge(next); } else { closeIfExpired(current, cutoffTime); mergedSessions.add(current); current = next; } } closeIfExpired(current, cutoffTime); mergedSessions.add(current);<br>if (mergedSessions.size() == 0) return Optional.absent();<br>return Optional.of(mergedSessions); } }class SessionDurationByWindow implements PairFlatMapFunction< Tuple2<String, List<Session>>, Long, Tuple2<Long, Integer>> { private Long windowDuration; SessionDurationByWindow(Long windowDuration) { this.windowDuration = windowDuration; }<br>@Override public Iterable<Tuple2<Long, Tuple2<Long, Integer>>> call( Tuple2<String, List<Session>> userSessions) { return userSessions ._2() .stream() .map(session  -> new Tuple2<Long, Tuple2<Long, Integer>>( (session.end / windowDuration) * windowDuration, new Tuple2<Long, Integer>(session.end - session.start, 1))) .collect(Collectors.toList()); } } |

Listing 5: The sessions portion of the Game Stats pipeline. [[Dataflow code](https://github.com/GoogleCloudPlatform/DataflowSDK-examples/blob/master-1.x/src/main/java8/com/google/cloud/dataflow/examples/complete/game/GameStats.java#L317), [Spark code](https://github.com/GoogleCloudPlatform/spark-examples/blob/master/gaming/java/src/main/java/com/google/cloud/sparkdemo/GameStats.java#L357)]

Semantically, the Spark version also suffers. As before, Spark is stuck with no real concept of event-time completeness. In response, we're forced to artificially delay emitting sessions for some arbitrary length of processing time in an attempt to catch as many data in the session as possible. This, of course, directly affects output latency. The other option would be to repeatedly emit all active sessions until they reach their individual garbage collection horizons, but this would result in a significant amount of network traffic and duplicated work as session are repeatedly emitted every micro-batch until they expire.

Thus, the Spark code delays output by an extra two hours of processing time, which means that it takes at least two hours from the time the last event in the session ends until that session will be materialized as an output by the Spark pipeline. This could be mitigated somewhat by increasing the flush timeout to something like 24 hours, but you then correspondingly increase the latency of your output; hello batch! Alternatively, you could perhaps track the number of micro-batches for which the session hasn't changed, and produce output after a sufficient period of inactivity. This is a bit closer to how heuristic watermarks effectively operate. However, watermark heuristics typically have more information at hand to utilize, for example: partitions, ordering within partitions if any, growth rates within partitions, etc. Simply relying on observed data rates for a single key would not yield a particularly robust heuristic watermark.

Contrast this to the Dataflow pipeline, where latency to output for any given session is only limited by the actual size of each individual session (i.e., the length of time from first element in the session to final element plus gap duration), and correctness (in the case of perfect watermarks, at least, and even for the most part with accurate heuristic watermarks) remains intact even in light of input delays, thanks to the system-wide tracking of event-time completeness.

Also, getting sessions right is not an easy task, especially when you start dealing with notions of completeness; there are a lot of subtleties involved, even in the simplistic Spark implementation we built for this post. Being able to just drop in a well-engineered and thoroughly tested sessions implementation, as you can with Dataflow, is actually a much bigger deal that it may seem at first blush.

One final note: [Spark 1.6.0](https://docs.cloud.databricks.com/docs/spark/1.6/index.html#Apache%20Spark%201.6%20Release%20Notes.html) introduced the `mapWithState` operation, which is a vast improvement over `updateStateByKey` in terms of performance and functionality. One of the nice things about `mapWithState` is that it allows you to build processing-time sessions quite naturally. That's still no help unless your data are guaranteed to always arrive strictly in order (i.e., kiss mobile goodbye), but it's a step in the right direction.

### Conclusion

To reiterate the point exemplified repeatedly throughout this post: Dataflow provides the flexibility and power necessary for the next generation of real-time data-processing systems, with a clear, practical, and robust approach to out-of-order processing. It goes without saying that we're very excited by the possibility of bringing all of this to an even larger audience, thanks to the creation of the [Apache Beam incubator project](http://incubator.apache.org/projects/beam.html) (which, incidentally, includes work from our friends at [Cloudera](http://blog.cloudera.com/blog/2016/01/spark-dataflow-joins-googles-dataflow-sdk/) and [PayPal](https://github.com/cloudera/spark-dataflow/pull/76) to begin bringing the Dataflow model to the Spark runtime).

The Dataflow model lets you write clean, modular code that evolves beautifully over time as needs change and expand. The model maps directly onto the four questions that are relevant in any out-of-order data processing pipeline:

- ***What* results are calculated?** Answered via transformations.
- ***Where* in event time are results calculated?** Answered via event-time windowing.
- ***When* in processing time are results materialized?** Answered via watermarks, triggers, and allowed lateness.
- ***How* do refinements of results relate?** Answered via accumulation modes (only one of which we touched upon in this post; see [Streaming 102](http://oreilly.com/ideas/the-world-beyond-batch-streaming-102) for details on the others).

There is no other system in existence which provides this degree of flexibility and power, period.

As a result, each of the four *What*/*Where*/*When*/*How* questions can be addressed by independent sections of code, with answers for each specific question swapped in and out with zero corresponding changes in code relevant to other questions. This provides great flexibility in choosing precisely what the nature and cost of your calculated results should be, even as your pipeline evolves, while additionally leaving your codebase vastly more maintainable and understandable.

In addition, the powerful out-of-order processing constructs in our model, such as watermarks and triggers, allow you to maintain eventual correctness of results within a single pipeline, while also offering low-latency speculation, the ability to refine results after the fact when upstream data change, and an easy way to cap the useful lifetime of data within your system.

There is no other system in existence which provides this degree of flexibility and power, period. Even better, because of the elegant and practical design of the model, that flexibility and power comes along with increased simplicity and clarity of code, all of which together translate into data parallel solutions that are much easier to build and maintain, cheaper to operate, and ultimately more effective at providing precisely the types of results increasingly demanded by modern business.

Was this page helpful? Let us know how we did:
star_border
star_border
star_border
star_border
star_border

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated June 1, 2017.