Audio Processing for Dummies · Michael-F-Bryan

# Audio Processing for Dummies

   **   October 27, 2019       ** 10 minutes read

 **  [rust](http://adventures.michaelfbryan.com/tags/rust/)  •  [audio](http://adventures.michaelfbryan.com/tags/audio/)

In my spare time I’m an emergency services volunteer, and one of the tasks our unit has is to run the radio network and keep track of what’s happening. This can be a pretty stressful job, especially when there’s lots of radio traffic, and it’s not unusual to miss words or entire transmissions.

To help with a personal project that could make the job easier I’d like to implement a basic component of audio processing, the [Noise Gate](https://en.wikipedia.org/wiki/Noise_gate).

The basic idea is to scan through an audio stream and split it into individual clips based on volume, similar to the algorithm mentioned [on this Rust Audio discourse thread](https://rust-audio.discourse.group/t/splitting-an-audio-stream-based-on-volume-silence/171?u=michael-f-bryan).

The code written in this article is available [on GitHub](https://github.com/Michael-F-Bryan/noise-gate). Feel free to browse through and steal code or inspiration. It’s also been published as a crate [on crates.io](http://adventures.michaelfbryan.com/posts/audio-processing-for-dummies/crates.io/crates/noise-gate).Note

If you found this useful or spotted a bug, let me know on the blog’s[issue tracker](https://github.com/Michael-F-Bryan/adventures.michaelfbryan.com)!

## What Even Is Audio?

We’ve all consumed audio media at some point, but have you ever stopped and wondered how it works under the hood?

At its core, audio works by rapidly reading the volume level (a “sample”), typically 44,100 times per second (44.1 kHz is called the [*Sample Rate*](https://en.wikipedia.org/wiki/Sampling_(signal_processing)#Sampling_rate)). These samples are then encoded using [*Pulse Code Modulation*](https://en.wikipedia.org/wiki/Pulse-code_modulation).

According to Wikipedia:

> Pulse-code modulation (PCM) is a method used to digitally represent sampled analog signals. It is the standard form of digital audio in computers, compact discs, digital telephony and other digital audio applications. In a PCM stream, the amplitude of the analog signal is sampled regularly at uniform intervals, and each sample is quantized to the nearest value within a range of digital steps.

If it helps, a sample can be thought of as how far a speaker/microphone’s membrane is deflected at a particular point in time.Tip

It’s not uncommon to record multiple audio tracks at a time, for example imagine multiple microphones were used to provide a sense of direction/perspective (see [Sound Localisation](https://en.wikipedia.org/wiki/Sound_localization) for more). These multiple tracks are usually referred to as *Channels*.

**TL;DR:** In Rust lingo, you can think of an audio stream as:

	type AudioStream = Vec<Frame>;
	type Frame = [Sample; N]; *// where `N` is the number of channels in the stream
	***type Sample = i16 | f32;

The audio formats you are used to (MP3, WAV, OGG) are just different ways to store an `AudioStream` on disk, along with some metadata describing the audio (artist, year, etc.), typically using tricks like compression or [Delta Encoding](https://en.wikipedia.org/wiki/Delta_encoding) to make the resulting file as small as possible.

If you’re wondering why compression is important, these are the numbers for a simple uncompressed audio stream with:

- 30 seconds of audio
- 44.1 kHz sample rate
- 2 channels (e.g. left and right speaker)
- bit depth of 16 (i.e. the samples are `i16`)

	sizeof(Sample) = 2 bytes
	sizeof(Frame) = 2 * sizeof(Sample) = 4 bytes
	sizeof(1 second) = sizeof(Frame) * 44100 = 176400 bytes
	full clip = 30 * sizeof(1 second) = 5292000 bytes = 5.3 MB

… That’s a lot of data!

## Finding Sample Data

If we want to implement a noise gate we’re going to need some sample clips to test it on.

I’ve found the Air Traffic Controller recordings from [LiveATC.net](https://www.liveatc.net/recordings.php) are reasonably similar to my target, with the added bonus that they’re publicly available.

One example:
  Your browser does not support the audio tag.

Our end goal is to create a library that can break audio streams up into chunks based on volume without caring where the audio originally came from (MP3 file, microphone, another function, etc.). We’ll start by using [the WAV format](https://en.wikipedia.org/wiki/WAV) because it’s simple and a really good crate ([hound](https://crates.io/crates/hound)) already exists for working with WAV files.

You can download the sample clip and convert it to WAV using `ffmpeg`:

	$ mkdir -p tests/data
	$ curl "https://forums.liveatc.net/index.php?action=dlattach;topic=15455.0;attach=10441" > a-turtle-of-an-issue.mp3
	$ ffmpeg -i a-turtle-of-an-issue.mp3 -ac 1 a-turtle-of-an-issue.wav

## Implementing the Noise Gate Algorithm

For now, our *Noise Gate* will have two knobs for tweaking its behaviour:

- `open_threshold` - the (absolute) noise value above which the gate should open
- `release_time` - how long to hold the gate open after dropping below the`open_threshold`. This will manifest itself as the gate being in a sort of half-open state for the next `release_time` samples, where new samples above the `open_threshold` will re-open the gate.

The awesome thing about this algorithm is that it can be represented using a simple state machine.

	*// src/lib.rs
	***
	enum State {
	    Open,
	    Closing { remaining_samples: usize },
	    Closed,
	}

Our state machine diagram looks roughly like this:

![](data:image/svg+xml,%3csvg id='mermaid-1573603131268' width='100%25' xmlns='http://www.w3.org/2000/svg' style='max-width: 558.875px%3b' viewBox='0 0 558.875 316' data-evernote-id='379' class='js-evernote-checked'%3e%3cstyle data-evernote-id='380' class='js-evernote-checked'%3e%23mermaid-1573603131268 .label%7bfont-family:'trebuchet ms'%2c verdana%2c arial%3bcolor:%23333%7d%23mermaid-1573603131268 .label text%7bfill:%23333%7d%23mermaid-1573603131268 .node rect%2c%23mermaid-1573603131268 .node circle%2c%23mermaid-1573603131268 .node ellipse%2c%23mermaid-1573603131268 .node polygon%7bfill:%23ECECFF%3bstroke:%239370db%3bstroke-width:1px%7d%23mermaid-1573603131268 .node.clickable%7bcursor:pointer%7d%23mermaid-1573603131268 .arrowheadPath%7bfill:%23333%7d%23mermaid-1573603131268 .edgePath .path%7bstroke:%23333%3bstroke-width:1.5px%7d%23mermaid-1573603131268 .edgeLabel%7bbackground-color:%23e8e8e8%7d%23mermaid-1573603131268 .cluster rect%7bfill:%23ffffde%3bstroke:%23aa3%3bstroke-width:1px%7d%23mermaid-1573603131268 .cluster text%7bfill:%23333%7d%23mermaid-1573603131268 div.mermaidTooltip%7bposition:absolute%3btext-align:center%3bmax-width:200px%3bpadding:2px%3bfont-family:'trebuchet ms'%2c verdana%2c arial%3bfont-size:12px%3bbackground:%23ffffde%3bborder:1px solid %23aa3%3bborder-radius:2px%3bpointer-events:none%3bz-index:100%7d%23mermaid-1573603131268 .actor%7bstroke:%23ccf%3bfill:%23ECECFF%7d%23mermaid-1573603131268 text.actor%7bfill:%23000%3bstroke:none%7d%23mermaid-1573603131268 .actor-line%7bstroke:grey%7d%23mermaid-1573603131268 .messageLine0%7bstroke-width:1.5%3bstroke-dasharray:'2 2'%3bstroke:%23333%7d%23mermaid-1573603131268 .messageLine1%7bstroke-width:1.5%3bstroke-dasharray:'2 2'%3bstroke:%23333%7d%23mermaid-1573603131268 %23arrowhead%7bfill:%23333%7d%23mermaid-1573603131268 .sequenceNumber%7bfill:%23fff%7d%23mermaid-1573603131268 %23sequencenumber%7bfill:%23333%7d%23mermaid-1573603131268 %23crosshead path%7bfill:%23333 !important%3bstroke:%23333 !important%7d%23mermaid-1573603131268 .messageText%7bfill:%23333%3bstroke:none%7d%23mermaid-1573603131268 .labelBox%7bstroke:%23ccf%3bfill:%23ECECFF%7d%23mermaid-1573603131268 .labelText%7bfill:%23000%3bstroke:none%7d%23mermaid-1573603131268 .loopText%7bfill:%23000%3bstroke:none%7d%23mermaid-1573603131268 .loopLine%7bstroke-width:2%3bstroke-dasharray:'2 2'%3bstroke:%23ccf%7d%23mermaid-1573603131268 .note%7bstroke:%23aa3%3bfill:%23fff5ad%7d%23mermaid-1573603131268 .noteText%7bfill:black%3bstroke:none%3bfont-family:'trebuchet ms'%2c verdana%2c arial%3bfont-size:14px%7d%23mermaid-1573603131268 .activation0%7bfill:%23f4f4f4%3bstroke:%23666%7d%23mermaid-1573603131268 .activation1%7bfill:%23f4f4f4%3bstroke:%23666%7d%23mermaid-1573603131268 .activation2%7bfill:%23f4f4f4%3bstroke:%23666%7d%23mermaid-1573603131268 .section%7bstroke:none%3bopacity:0.2%7d%23mermaid-1573603131268 .section0%7bfill:rgba(102%2c102%2c255%2c0.49)%7d%23mermaid-1573603131268 .section2%7bfill:%23fff400%7d%23mermaid-1573603131268 .section1%2c%23mermaid-1573603131268 .section3%7bfill:%23fff%3bopacity:0.2%7d%23mermaid-1573603131268 .sectionTitle0%7bfill:%23333%7d%23mermaid-1573603131268 .sectionTitle1%7bfill:%23333%7d%23mermaid-1573603131268 .sectionTitle2%7bfill:%23333%7d%23mermaid-1573603131268 .sectionTitle3%7bfill:%23333%7d%23mermaid-1573603131268 .sectionTitle%7btext-anchor:start%3bfont-size:11px%3btext-height:14px%7d%23mermaid-1573603131268 .grid .tick%7bstroke:%23d3d3d3%3bopacity:0.3%3bshape-rendering:crispEdges%7d%23mermaid-1573603131268 .grid path%7bstroke-width:0%7d%23mermaid-1573603131268 .today%7bfill:none%3bstroke:red%3bstroke-width:2px%7d%23mermaid-1573603131268 .task%7bstroke-width:2%7d%23mermaid-1573603131268 .taskText%7btext-anchor:middle%3bfont-size:11px%7d%23mermaid-1573603131268 .taskTextOutsideRight%7bfill:%23000%3btext-anchor:start%3bfont-size:11px%7d%23mermaid-1573603131268 .taskTextOutsideLeft%7bfill:%23000%3btext-anchor:end%3bfont-size:11px%7d%23mermaid-1573603131268 .task.clickable%7bcursor:pointer%7d%23mermaid-1573603131268 .taskText.clickable%7bcursor:pointer%3bfill:%23003163 !important%3bfont-weight:bold%7d%23mermaid-1573603131268 .taskTextOutsideLeft.clickable%7bcursor:pointer%3bfill:%23003163 !important%3bfont-weight:bold%7d%23mermaid-1573603131268 .taskTextOutsideRight.clickable%7bcursor:pointer%3bfill:%23003163 !important%3bfont-weight:bold%7d%23mermaid-1573603131268 .taskText0%2c%23mermaid-1573603131268 .taskText1%2c%23mermaid-1573603131268 .taskText2%2c%23mermaid-1573603131268 .taskText3%7bfill:%23fff%7d%23mermaid-1573603131268 .task0%2c%23mermaid-1573603131268 .task1%2c%23mermaid-1573603131268 .task2%2c%23mermaid-1573603131268 .task3%7bfill:%238a90dd%3bstroke:%23534fbc%7d%23mermaid-1573603131268 .taskTextOutside0%2c%23mermaid-1573603131268 .taskTextOutside2%7bfill:%23000%7d%23mermaid-1573603131268 .taskTextOutside1%2c%23mermaid-1573603131268 .taskTextOutside3%7bfill:%23000%7d%23mermaid-1573603131268 .active0%2c%23mermaid-1573603131268 .active1%2c%23mermaid-1573603131268 .active2%2c%23mermaid-1573603131268 .active3%7bfill:%23bfc7ff%3bstroke:%23534fbc%7d%23mermaid-1573603131268 .activeText0%2c%23mermaid-1573603131268 .activeText1%2c%23mermaid-1573603131268 .activeText2%2c%23mermaid-1573603131268 .activeText3%7bfill:%23000 !important%7d%23mermaid-1573603131268 .done0%2c%23mermaid-1573603131268 .done1%2c%23mermaid-1573603131268 .done2%2c%23mermaid-1573603131268 .done3%7bstroke:grey%3bfill:%23d3d3d3%3bstroke-width:2%7d%23mermaid-1573603131268 .doneText0%2c%23mermaid-1573603131268 .doneText1%2c%23mermaid-1573603131268 .doneText2%2c%23mermaid-1573603131268 .doneText3%7bfill:%23000 !important%7d%23mermaid-1573603131268 .crit0%2c%23mermaid-1573603131268 .crit1%2c%23mermaid-1573603131268 .crit2%2c%23mermaid-1573603131268 .crit3%7bstroke:%23f88%3bfill:red%3bstroke-width:2%7d%23mermaid-1573603131268 .activeCrit0%2c%23mermaid-1573603131268 .activeCrit1%2c%23mermaid-1573603131268 .activeCrit2%2c%23mermaid-1573603131268 .activeCrit3%7bstroke:%23f88%3bfill:%23bfc7ff%3bstroke-width:2%7d%23mermaid-1573603131268 .doneCrit0%2c%23mermaid-1573603131268 .doneCrit1%2c%23mermaid-1573603131268 .doneCrit2%2c%23mermaid-1573603131268 .doneCrit3%7bstroke:%23f88%3bfill:%23d3d3d3%3bstroke-width:2%3bcursor:pointer%3bshape-rendering:crispEdges%7d%23mermaid-1573603131268 .milestone%7btransform:rotate(45deg) scale(0.8%2c 0.8)%7d%23mermaid-1573603131268 .milestoneText%7bfont-style:italic%7d%23mermaid-1573603131268 .doneCritText0%2c%23mermaid-1573603131268 .doneCritText1%2c%23mermaid-1573603131268 .doneCritText2%2c%23mermaid-1573603131268 .doneCritText3%7bfill:%23000 !important%7d%23mermaid-1573603131268 .activeCritText0%2c%23mermaid-1573603131268 .activeCritText1%2c%23mermaid-1573603131268 .activeCritText2%2c%23mermaid-1573603131268 .activeCritText3%7bfill:%23000 !important%7d%23mermaid-1573603131268 .titleText%7btext-anchor:middle%3bfont-size:18px%3bfill:%23000%7d%23mermaid-1573603131268 g.classGroup text%7bfill:%239370db%3bstroke:none%3bfont-family:'trebuchet ms'%2c verdana%2c arial%3bfont-size:10px%7d%23mermaid-1573603131268 g.classGroup rect%7bfill:%23ECECFF%3bstroke:%239370db%7d%23mermaid-1573603131268 g.classGroup line%7bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 .classLabel .box%7bstroke:none%3bstroke-width:0%3bfill:%23ECECFF%3bopacity:0.5%7d%23mermaid-1573603131268 .classLabel .label%7bfill:%239370db%3bfont-size:10px%7d%23mermaid-1573603131268 .relation%7bstroke:%239370db%3bstroke-width:1%3bfill:none%7d%23mermaid-1573603131268 %23compositionStart%7bfill:%239370db%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23compositionEnd%7bfill:%239370db%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23aggregationStart%7bfill:%23ECECFF%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23aggregationEnd%7bfill:%23ECECFF%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23dependencyStart%7bfill:%239370db%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23dependencyEnd%7bfill:%239370db%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23extensionStart%7bfill:%239370db%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 %23extensionEnd%7bfill:%239370db%3bstroke:%239370db%3bstroke-width:1%7d%23mermaid-1573603131268 .commit-id%2c%23mermaid-1573603131268 .commit-msg%2c%23mermaid-1573603131268 .branch-label%7bfill:lightgrey%3bcolor:lightgrey%7d %3c/style%3e%3cstyle data-evernote-id='381' class='js-evernote-checked'%3e%23mermaid-1573603131268 %7b color: rgb(33%2c 33%2c 33)%3b font: normal normal 300 normal 16px / 28.8px Merriweather%2c Georgia%2c serif%3b %7d%3c/style%3e%3cg transform='translate(-12%2c -12)' data-evernote-id='382' class='js-evernote-checked'%3e%3cg class='output js-evernote-checked' data-evernote-id='383'%3e%3cg class='clusters js-evernote-checked' data-evernote-id='384'%3e%3c/g%3e%3cg class='edgePaths js-evernote-checked' data-evernote-id='385'%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='386'%3e%3cpath class='path js-evernote-checked' d='M265.34375%2c52.975196589990446L234.95703125%2c61.97933049165871C204.5703125%2c70.98346439332697%2c143.796875%2c88.99173219666348%2c120.92578125%2c104.49586609833175C98.0546875%2c120%2c113.0859375%2c133%2c120.6015625%2c139.5L128.1171875%2c146' marker-end='url(%23arrowhead25)' style='fill:none' data-evernote-id='387'%3e%3c/path%3e%3cdefs data-evernote-id='388' class='js-evernote-checked'%3e%3cmarker id='arrowhead25' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='389' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='390'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='391'%3e%3cpath class='path js-evernote-checked' d='M325.921875%2c36.37998525919253L336.7734375%2c33.649987715993774C347.625%2c30.91999017279502%2c369.328125%2c25.45999508639751%2c382.892578125%2c22.729997543198753C396.45703125%2c20%2c401.8828125%2c20%2c407.30859375%2c24C412.734375%2c28%2c418.16015625%2c36%2c418.16015625%2c44C418.16015625%2c52%2c412.734375%2c60%2c407.30859375%2c64C401.8828125%2c68%2c396.45703125%2c68%2c382.892578125%2c65.27000245680124C369.328125%2c62.540004913602495%2c347.625%2c57.08000982720498%2c336.7734375%2c54.350012284006226L325.921875%2c51.62001474080747' marker-end='url(%23arrowhead26)' style='fill:none' data-evernote-id='392'%3e%3c/path%3e%3cdefs data-evernote-id='393' class='js-evernote-checked'%3e%3cmarker id='arrowhead26' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='394' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='395'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='396'%3e%3cpath class='path js-evernote-checked' d='M183.6171875%2c146L191.1328125%2c139.5C198.6484375%2c133%2c213.6796875%2c120%2c228.0999503968254%2c107C242.5202132936508%2c94%2c256.3294890873016%2c81%2c263.234126984127%2c74.5L270.1387648809524%2c68' marker-end='url(%23arrowhead27)' style='fill:none' data-evernote-id='397'%3e%3c/path%3e%3cdefs data-evernote-id='398' class='js-evernote-checked'%3e%3cmarker id='arrowhead27' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='399' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='400'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='401'%3e%3cpath class='path js-evernote-checked' d='M155.8671875%2c194L155.8671875%2c200.5C155.8671875%2c207%2c155.8671875%2c220%2c178.59244791666666%2c234.81547781105363C201.31770833333334%2c249.63095562210728%2c246.76822916666666%2c266.26191124421456%2c269.4934895833333%2c274.57738905526816L292.21875%2c282.8928668663218' marker-end='url(%23arrowhead28)' style='fill:none' data-evernote-id='402'%3e%3c/path%3e%3cdefs data-evernote-id='403' class='js-evernote-checked'%3e%3cmarker id='arrowhead28' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='404' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='405'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='406'%3e%3cpath class='path js-evernote-checked' d='M195.015625%2c162.48303018938682L209.32291666666666%2c159.73585849115568C223.63020833333334%2c156.98868679292454%2c252.24479166666666%2c151.49434339646226%2c270.12890625%2c148.74717169823114C288.0130208333333%2c146%2c295.1666666666667%2c146%2c302.3203125%2c150C309.4739583333333%2c154%2c316.6276041666667%2c162%2c316.6276041666667%2c170C316.6276041666667%2c178%2c309.4739583333333%2c186%2c302.3203125%2c190C295.1666666666667%2c194%2c288.0130208333333%2c194%2c270.12890625%2c191.25282830176886C252.24479166666666%2c188.50565660353774%2c223.63020833333334%2c183.01131320707546%2c209.32291666666666%2c180.26414150884432L195.015625%2c177.51696981061318' marker-end='url(%23arrowhead29)' style='fill:none' data-evernote-id='407'%3e%3c/path%3e%3cdefs data-evernote-id='408' class='js-evernote-checked'%3e%3cmarker id='arrowhead29' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='409' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='410'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='411'%3e%3cpath class='path js-evernote-checked' d='M363.859375%2c282.8928668663218L386.5846354166667%2c274.57738905526816C409.3098958333333%2c266.26191124421456%2c454.7604166666667%2c249.63095562210728%2c477.4856770833333%2c230.81547781105363C500.2109375%2c212%2c500.2109375%2c191%2c500.2109375%2c170C500.2109375%2c149%2c500.2109375%2c128%2c471.1627604166667%2c108.55459023905904C442.1145833333333%2c89.10918047811806%2c384.0182291666667%2c71.21836095623615%2c354.9700520833333%2c62.272951195295185L325.921875%2c53.32754143435423' marker-end='url(%23arrowhead30)' style='fill:none' data-evernote-id='412'%3e%3c/path%3e%3cdefs data-evernote-id='413' class='js-evernote-checked'%3e%3cmarker id='arrowhead30' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='414' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='415'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3cg class='edgePath js-evernote-checked' style='opacity: 1%3b' data-evernote-id='416'%3e%3cpath class='path js-evernote-checked' d='M363.859375%2c287.5024839764215L374.7508680555556%2c284.9187366470179C385.6423611111111%2c282.3349893176143%2c407.4253472222222%2c277.16749465880713%2c421.0397135416666%2c274.5837473294036C434.6540798611111%2c272%2c440.0998263888889%2c272%2c445.5455729166667%2c276C450.9913194444445%2c280%2c456.43706597222223%2c288%2c456.4370659722222%2c296C456.43706597222223%2c304%2c450.9913194444445%2c312%2c445.54557291666674%2c316C440.0998263888889%2c320%2c434.6540798611111%2c320%2c421.0397135416667%2c317.4162526705964C407.4253472222222%2c314.83250534119287%2c385.6423611111111%2c309.6650106823857%2c374.7508680555555%2c307.0812633529821L363.859375%2c304.4975160235785' marker-end='url(%23arrowhead31)' style='fill:none' data-evernote-id='417'%3e%3c/path%3e%3cdefs data-evernote-id='418' class='js-evernote-checked'%3e%3cmarker id='arrowhead31' viewBox='0 0 10 10' refX='9' refY='5' markerUnits='strokeWidth' markerWidth='8' markerHeight='6' orient='auto' data-evernote-id='419' class='js-evernote-checked'%3e%3cpath d='M 0 0 L 10 5 L 0 10 z' class='arrowheadPath js-evernote-checked' style='stroke-width: 1%3b stroke-dasharray: 1%2c 0%3b' data-evernote-id='420'%3e%3c/path%3e%3c/marker%3e%3c/defs%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabels js-evernote-checked' data-evernote-id='421'%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(83.0234375%2c107)' style='opacity: 1%3b' data-evernote-id='422'%3e%3cg transform='translate(-63.0234375%2c-14)' class='label js-evernote-checked' data-evernote-id='423'%3e%3cforeignObject width='126.046875' height='28' data-evernote-id='424' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='425' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='426'%3ebelow threshold%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(423.5859375%2c44)' style='opacity: 1%3b' data-evernote-id='427'%3e%3cg transform='translate(-62.6640625%2c-14)' class='label js-evernote-checked' data-evernote-id='428'%3e%3cforeignObject width='125.328125' height='28' data-evernote-id='429' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='430' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='431'%3eabove threshold%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(228.7109375%2c107)' style='opacity: 1%3b' data-evernote-id='432'%3e%3cg transform='translate(-62.6640625%2c-14)' class='label js-evernote-checked' data-evernote-id='433'%3e%3cforeignObject width='125.328125' height='28' data-evernote-id='434' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='435' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='436'%3eabove threshold%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(155.8671875%2c233)' style='opacity: 1%3b' data-evernote-id='437'%3e%3cg transform='translate(-93.6328125%2c-14)' class='label js-evernote-checked' data-evernote-id='438'%3e%3cforeignObject width='187.265625' height='28' data-evernote-id='439' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='440' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='441'%3eremaining_samples = 0%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(323.78125%2c170)' style='opacity: 1%3b' data-evernote-id='442'%3e%3cg transform='translate(-93.765625%2c-14)' class='label js-evernote-checked' data-evernote-id='443'%3e%3cforeignObject width='187.53125' height='28' data-evernote-id='444' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='445' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='446'%3eremaining_samples %26gt%3b 0%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(500.2109375%2c170)' style='opacity: 1%3b' data-evernote-id='447'%3e%3cg transform='translate(-62.6640625%2c-14)' class='label js-evernote-checked' data-evernote-id='448'%3e%3cforeignObject width='125.328125' height='28' data-evernote-id='449' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='450' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='451'%3eabove threshold%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3cg class='edgeLabel js-evernote-checked' transform='translate(461.8828125%2c296)' style='opacity: 1%3b' data-evernote-id='452'%3e%3cg transform='translate(-63.0234375%2c-14)' class='label js-evernote-checked' data-evernote-id='453'%3e%3cforeignObject width='126.046875' height='28' data-evernote-id='454' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='455' class='js-evernote-checked'%3e%3cspan class='edgeLabel js-evernote-checked' data-evernote-id='456'%3ebelow threshold%3c/span%3e%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3c/g%3e%3cg class='nodes js-evernote-checked' data-evernote-id='457'%3e%3cg class='node js-evernote-checked' id='Open' transform='translate(295.6328125%2c44)' style='opacity: 1%3b' data-evernote-id='458'%3e%3crect rx='0' ry='0' x='-30.2890625' y='-24' width='60.578125' height='48' data-evernote-id='459' class='js-evernote-checked'%3e%3c/rect%3e%3cg class='label js-evernote-checked' transform='translate(0%2c0)' data-evernote-id='460'%3e%3cg transform='translate(-20.2890625%2c-14)' data-evernote-id='461' class='js-evernote-checked'%3e%3cforeignObject width='40.578125' height='28' data-evernote-id='462' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='463' class='js-evernote-checked'%3eOpen%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3c/g%3e%3cg class='node js-evernote-checked' id='Closing' transform='translate(155.8671875%2c170)' style='opacity: 1%3b' data-evernote-id='464'%3e%3crect rx='5' ry='5' x='-39.1484375' y='-24' width='78.296875' height='48' data-evernote-id='465' class='js-evernote-checked'%3e%3c/rect%3e%3cg class='label js-evernote-checked' transform='translate(0%2c0)' data-evernote-id='466'%3e%3cg transform='translate(-29.1484375%2c-14)' data-evernote-id='467' class='js-evernote-checked'%3e%3cforeignObject width='58.296875' height='28' data-evernote-id='468' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='469' class='js-evernote-checked'%3eClosing%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3c/g%3e%3cg class='node js-evernote-checked' id='Closed' transform='translate(328.0390625%2c296)' style='opacity: 1%3b' data-evernote-id='470'%3e%3crect rx='0' ry='0' x='-35.8203125' y='-24' width='71.640625' height='48' data-evernote-id='471' class='js-evernote-checked'%3e%3c/rect%3e%3cg class='label js-evernote-checked' transform='translate(0%2c0)' data-evernote-id='472'%3e%3cg transform='translate(-25.8203125%2c-14)' data-evernote-id='473' class='js-evernote-checked'%3e%3cforeignObject width='51.640625' height='28' data-evernote-id='474' class='js-evernote-checked'%3e%3cdiv xmlns='http://www.w3.org/1999/xhtml' style='display: inline-block%3b white-space: nowrap%3b' data-evernote-id='475' class='js-evernote-checked'%3eClosed%3c/div%3e%3c/foreignObject%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/g%3e%3c/svg%3e)

We’ll be using some abstractions, namely [`Frame`](https://docs.rs/sample/latest/sample/frame/trait.Frame.html) and[`Sample`](https://docs.rs/sample/latest/sample/trait.Sample.html) from the [`sample` crate](https://crates.io/crates/sample), to make the*Noise Gate* work with multiple channels and any type of audio input.

Let’s define a helper which will take a `Frame` of audio input and tell us whether all audio channels are below a certain threshold.

	*// src/lib.rs
	***
	use sample::{Frame, SignedSample};

	fn below_threshold<F>(frame: F, threshold: F::Sample) -> bool
	where
	    F: Frame,
	{
	    let threshold = abs(threshold.to_signed_sample());

	    frame
	        .channels()
	        .map(|sample| sample.to_signed_sample())
	        .map(abs)
	        .all(|sample| sample < threshold)
	}

	fn abs<S: SignedSample>(sample: S) -> S {
	    let zero = S::equilibrium();
	    if sample >= zero {
	        sample
	    } else {
	        -sample
	    }
	}

The `State` transitions are done using one big `match` statement and are almost a direct translation of the previous state machine diagram.

	*// src/lib.rs
	***
	fn next_state<F: Frame>(
	    state: State,
	    frame: F,
	    open_threshold: F::Sample,
	    release_time: usize,
	) -> State {
	    match state {
	        State::Open => {
	            if below_threshold(frame, open_threshold) {
	                State::Closing {
	                    remaining_samples: release_time,
	                }
	            } else {
	                State::Open
	            }
	        }

	        State::Closing { remaining_samples } => {
	            if below_threshold(frame, open_threshold) {
	                if remaining_samples == 0 {
	                    State::Closed
	                } else {
	                    State::Closing {
	                        remaining_samples: remaining_samples - 1,
	                    }
	                }
	            } else {
	                State::Open
	            }
	        }

	        State::Closed => {
	            if below_threshold(frame, open_threshold) {
	                State::Closed
	            } else {
	                State::Open
	            }
	        }
	    }
	}

There’s a bit more rightward drift here than I’d like, but the function itself is quite self-contained and readable enough.

That said, as a sanity check it’s a good idea to write some tests exercising each state machine transition.

	*// src/lib.rs
	***
	#[cfg(test)]
	mod tests {
	    use super::*;

	    const OPEN_THRESHOLD: i16 = 100;
	    const RELEASE_TIME: usize = 5;

	    test_state_transition!(open_to_open: State::Open, 101 => State::Open);
	    test_state_transition!(open_to_closing: State::Open, 40 => State::Closing { remaining_samples: RELEASE_TIME });
	    test_state_transition!(closing_to_closed: State::Closing { remaining_samples: 0 }, 40 => State::Closed);
	    test_state_transition!(closing_to_closing: State::Closing { remaining_samples: 1 }, 40 => State::Closing { remaining_samples: 0 });
	    test_state_transition!(reopen_when_closing: State::Closing { remaining_samples: 1 }, 101 => State::Open);
	    test_state_transition!(closed_to_closed: State::Closed, 40 => State::Closed);
	    test_state_transition!(closed_to_open: State::Closed, 101 => State::Open);
	}

When writing these sorts of tests you’ll probably want to minimise boilerplate by pulling the testing code out into a macro. That way you just need to write to case being tested, inputs, and expected outputs, and the macro will do the rest.Tip

This is the definition for `test_state_transition!()`:

	macro_rules! test_state_transition {
	    ($name:ident, $from:expr, $sample:expr => $expected:expr) => {
	        #[test]
	        fn $name() {
	            let start: State = $from;
	            let expected: State = $expected;
	            let frame: [i16; 1] = [$sample];

	            let got = next_state(start, frame, OPEN_THRESHOLD, RELEASE_TIME);

	            assert_eq!(got, expected);
	        }
	    };
	}

To implement the *Noise Gate*, we’ll wrap our state and configuration into a single `NoiseGate` struct.

	*// src/lib.rs
	***
	pub struct NoiseGate<S> {
	    */// The volume level at which the gate will open (begin recording).
	***    pub open_threshold: S,
	    */// The amount of time (in samples) the gate takes to go from open to fully
	***    */// closed.
	***    pub release_time: usize,
	    state: State,
	}

	impl<S> NoiseGate<S> {
	    */// Create a new [`NoiseGate`].
	***    pub const fn new(open_threshold: S, release_time: usize) -> Self {
	        NoiseGate {
	            open_threshold,
	            release_time,
	            state: State::Closed,
	        }
	    }

	    */// Is the gate currently passing samples through to the [`Sink`]?
	***    pub fn is_open(&self) -> bool {
	        match self.state {
	            State::Open | State::Closing { .. } => true,
	            State::Closed => false,
	        }
	    }

	    */// Is the gate currently ignoring silence?
	***    pub fn is_closed(&self) -> bool {
	        !self.is_open()
	    }
	}

We’ll need to declare a `Sink` trait that can be implemented by consumers of our *Noise Gate* in the next step.

	*// src/lib.rs
	***
	pub trait Sink<F> {
	    */// Add a frame to the current recording, starting a new recording if
	***    */// necessary.
	***    fn record(&mut self, frame: F);
	    */// Reached the end of the samples, do necessary cleanup (e.g. flush to disk).
	***    fn end_of_transmission(&mut self);
	}

Processing frames is just a case of iterating over each frame, updating the state, and checking whether we need to pass the frame through to the `Sink` or detect an `end_of_transmission`.

	*// src/lib.rs
	***
	impl<S: Sample> NoiseGate<S> {
	    pub fn process_frames<K, F>(&mut self, frames: &[F], sink: &mut K)
	    where
	        F: Frame<Sample = S>,
	        K: Sink<F>,
	    {
	        for &frame in frames {
	            let previously_open = self.is_open();

	            self.state = next_state(self.state, frame, self.open_threshold, self.release_time);

	            if self.is_open() {
	                sink.record(frame);
	            } else if previously_open {
	                *// the gate was previously open and has just closed
	***                sink.end_of_transmission();
	            }
	        }
	    }
	}

## Measuring Performance

If we want to use the `NoiseGate` in realtime applications we’ll need to make sure it can handle typical sample rates.

I don’t expect our algorithm to add much in terms of a performance overhead, but it’s always a good idea to check.

The gold standard for benchmarking in Rust is [criterion](https://github.com/bheisler/criterion.rs), so let’s add that as a dev dependency.

	*# Cargo.toml*

	[dev-dependencies]
	criterion = "0.3"

	[[bench]]
	name = "throughput"
	harness = false

We’ll need a `Sink` implementation which will add as little overhead as possible without being completely optimised out by the compiler.

	*// benches/throughput.rs
	***
	struct Counter {
	    samples: usize,
	    chunks: usize,
	}

	impl<F> Sink<F> for Counter {
	    fn record(&mut self, _: F) {
	        self.samples += criterion::black_box(1);
	    }

	    fn end_of_transmission(&mut self) {
	        self.chunks += criterion::black_box(1);
	    }
	}

We’ve already downloaded a handful of example WAV files to the `data/`directory, so we can register a new benchmark group (a group of related benchmarks which should be graphed together) and register a benchmark for every WAV file in the `data/` directory.

	*// benches/throughput.rs
	***
	const DATA_DIR: &str = concat!(env!("CARGO_MANIFEST_DIR"), "/data/");

	fn bench_throughput(c: &mut Criterion) {
	    let mut group = c.benchmark_group("throughput");

	    for entry in fs::read_dir(DATA_DIR).unwrap() {
	        let entry = entry.unwrap();
	        let path = entry.path();

	        if path.is_file() {
	            let name = path.file_stem().unwrap().to_str().unwrap();
	            add_benchmark(&mut group, name, &path);
	        }
	    }
	}

The setup work for each WAV file benchmark is non-trivial, so we’ve pulled it out into its own function. To set things up we’ll use [`hound`](https://crates.io/crates/hound) to read the entire audio clip into a `Vec<[i16; 1]>` in memory and guess a reasonable`release_time` and `noise_threshold`.

Then it’s just a case of telling the `BenchmarkGroup` how many samples we’re working with (throughput) and processing the frames.

	*// benches/throughput.rs
	***
	fn add_benchmark(
	    group: &mut BenchmarkGroup<WallTime>,
	    name: &str,
	    path: &Path,
	) {
	    let reader = WavReader::open(path).unwrap();

	    let desc = reader.spec();
	    assert_eq!(desc.channels, 1, "We've hard-coded frames to be [i16; 1]");
	    let release_time = 2 * desc.sample_rate as usize;

	    let samples = reader
	        .into_samples::<i16>()
	        .map(|s| [s.unwrap()])
	        .collect::<Vec<_>>();

	    let noise_threshold = average(&samples);

	    group
	        .throughput(Throughput::Elements(samples.len() as u64))
	        .bench_function(name, |b| {
	            b.iter(|| {
	                let mut counter = Counter::default();
	                let mut gate = NoiseGate::new(noise_threshold, release_time);
	                gate.process_frames(&samples, &mut counter);
	            });
	        });
	}

	*/// A fancy way to add up all the channels in all the frames and get the average
	**/// sample value.
	***fn average<F>(samples: &[F]) -> F::Sample
	where
	    F: Frame,
	    F::Sample: FromSample<f32>,
	    F::Sample: ToSample<f32>,
	{
	    let sum: f32 = samples.iter().fold(0.0, |sum, frame| {
	        sum + frame.channels().map(|s| s.to_sample()).sum::<f32>()
	    });
	    (sum / samples.len() as f32).round().to_sample()
	}

Finally, we need to invoke a couple macros to register the `"throughput"`benchmark group and create a `main` function (remember when declaring the`[[bench]]` table we told `rustc` not to write `main()` for us with `harness = false`).

	*// benches/throughput.rs
	***
	criterion_group!(benches, bench_throughput);
	criterion_main!(benches);

These are the WAV files I’ve downloaded to the `data/` directory:

	$ ls -l data
	.rw-r--r-- 1.6M michael 27 Oct 21:21 a-turtle-of-an-issue.wav
	.rw-r--r-- 4.2M michael 27 Oct 21:17 KBDL-B17-Tribute-20191005.wav
	.rw-r--r-- 7.6M michael 27 Oct 21:17 N11379_KSCK.wav
	.rw-r--r--  12M michael 27 Oct 21:26 tornado-warning-ground.wav
	$ file data/*
	data/a-turtle-of-an-issue.wav:      RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 22050 Hz
	data/KBDL-B17-Tribute-20191005.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 24000 Hz
	data/N11379_KSCK.wav:               RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 22050 Hz
	data/tornado-warning-ground.wav:    RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz

Now let’s run the benchmarks.

	$ cargo bench
	     Running target/release/deps/throughput-dbdb305fc8a0e002
	Benchmarking throughput/a-turtle-of-an-issue: Warming up for 3.0000 s
	Warning: Unable to complete 100 samples in 5.0s. You may wish to increase target time to 37.5s or reduce sample count to 20
	throughput/a-turtle-of-an-issue
	                        time:   [7.0509 ms 7.1617 ms 7.2892 ms]
	                        thrpt:  [113.14 Melem/s 115.15 Melem/s 116.96 Melem/s]
	                 change:
	                        time:   [-6.5194% -3.2691% -0.1646%] (p = 0.07 > 0.05)
	                        thrpt:  [+0.1648% +3.3796% +6.9740%]
	                        No change in performance detected.
	Found 9 outliers among 100 measurements (9.00%)
	  8 (8.00%) high mild
	  1 (1.00%) high severe

	...

If you’ve got `gnuplot` installed, this also generates [a report](http://adventures.michaelfbryan.com/criterion/report/index.html)under `target/criterion`.

On my machine the report says our `NoiseFilter` can process 103.47 million samples per second. This is about 2000 times faster than we need, so it gives us hope that the *algorithm* won’t add any unnecessary overhead… Of course that just moves the bottleneck from `NoiseFilter` to the caller’s `Sink`implementation.

## Experimenting With Our Sample Data

We’re now at the point where we have a fully implemented *Noise Gate*. Let’s create an example program for splitting WAV files and see what happens when we point it at our sample data!

Even though it’s an example, we should probably implement proper command-line argument handling to make experimentation easier. By far the easiest way to do this is with [the structopt crate](https://crates.io/crates/structopt).

	*// examples/wav-splitter.rs
	***
	#[derive(Debug, Clone, StructOpt)]
	pub struct Args {
	    #[structopt(help = "The WAV file to read")]
	    pub input_file: PathBuf,
	    #[structopt(short = "t", long = "threshold", help = "The noise threshold")]
	    pub noise_threshold: i16,
	    #[structopt(
	        short = "r",
	        long = "release-time",
	        help = "The release time in seconds",
	        default_value = "0.25"
	    )]
	    pub release_time: f32,
	    #[structopt(
	        short = "o",
	        long = "output-dir",
	        help = "Where to write the split files",
	        default_value = "."
	    )]
	    pub output_dir: PathBuf,
	    #[structopt(
	        short = "p",
	        long = "prefix",
	        help = "A prefix to insert before each clip",
	        default_value = "clip_"
	    )]
	    pub prefix: String,
	}

Now we’ll need a `Sink` type. The general idea is every time the `record()`method is called we’ll write another frame to a cached `hound::WavWriter`. If the `WavWriter` doesn’t exist we’ll need to create a new one which writes to a file named like `output_dir/clip_1.wav`. An `end_of_transmission()` tells us to `finalize()` the `WavWriter` and remove it from our cache.

	*// examples/wav-splitter.rs
	***
	pub struct Sink {
	    output_dir: PathBuf,
	    clip_number: usize,
	    prefix: String,
	    spec: WavSpec,
	    writer: Option<WavWriter<BufWriter<File>>>,
	}

	impl Sink {
	    pub fn new(output_dir: PathBuf, prefix: String, spec: WavSpec) -> Self {
	        Sink {
	            output_dir,
	            prefix,
	            spec,
	            clip_number: 0,
	            writer: None,
	        }
	    }

	    fn get_writer(&mut self) -> &mut WavWriter<BufWriter<File>> {
	        if self.writer.is_none() {
	            let filename = self
	                .output_dir
	                .join(format!("{}{}.wav", self.prefix, self.clip_number));
	            self.clip_number += 1;
	            self.writer = Some(WavWriter::create(filename, self.spec).unwrap());
	        }

	        self.writer.as_mut().unwrap()
	    }
	}

	impl<F> noise_gate::Sink<F> for Sink
	where
	    F: Frame,
	    F::Sample: hound::Sample,
	{
	    fn record(&mut self, frame: F) {
	        let writer = self.get_writer();

	        for channel in frame.channels() {
	            writer.write_sample(channel).unwrap();
	        }
	    }

	    fn end_of_transmission(&mut self) {
	        if let Some(writer) = self.writer.take() {
	            writer.finalize().unwrap();
	        }
	    }
	}

From there the `main` function is quite simple. It parses some arguments, reads the WAV file into memory, then throws it at our `NoiseGate` so the `Sink` can write the clips to the `output/` directory.

	*// examples/wav-splitter.rs
	***
	fn main() -> Result<(), Box<dyn Error>> {
	    let args = Args::from_args();

	    let reader = WavReader::open(&args.input_file)?;
	    let header = reader.spec();
	    let samples = reader
	        .into_samples::<i16>()
	        .map(|result| result.map(|sample| [sample]))
	        .collect::<Result<Vec<_>, _>>()?;

	    let release_time = (header.sample_rate as f32 * args.release_time).round();

	    fs::create_dir_all(&args.output_dir)?;
	    let mut sink = Sink::new(args.output_dir, args.prefix, header);

	    let mut gate = NoiseGate::new(args.noise_threshold, release_time as usize);
	    gate.process_frames(&samples, &mut sink);

	    Ok(())
	}

Let’s take this for a test-run.
The original clip:
  Your browser does not support the audio tag.

Now let’s split it into pieces with our `wav-splitter` program. At this point I don’t really know what values of `noise_threshold` or `release_time` are acceptible for this audio, but I figure `50` and `0.3s` should be usable?

	$ ./target/release/examples/wav-splitter -o output --threshold 50 --release-time 0.3 data/N11379_KSCK.wav
	$ ls output
	clip_0.wav clip_3.wav clip_6.wav clip_9.wav clip_12.wav clip_15.wav
	clip_18.wav clip_21.wav clip_1.wav clip_4.wav clip_7.wav clip_10.wav
	clip_13.wav clip_16.wav clip_19.wav clip_22.wav clip_2.wav clip_5.wav
	clip_8.wav clip_11.wav clip_14.wav clip_17.wav clip_20.wav

Wow it actually worked on the first try. Now that’s something you don’t see every day.