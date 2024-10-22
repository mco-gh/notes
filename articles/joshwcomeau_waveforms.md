joshwcomeau/waveforms

# Waveforms

[(L)](https://github.com/joshwcomeau/waveforms/blob/master/demo.gif)

[![Convergence Demo](../_resources/4a6bb35b26aeab790a49c6205a4f47a4.gif)](https://github.com/joshwcomeau/waveforms/blob/master/demo.gif)

This interactive guide introduces and explores waveforms. It covers how to read waveform graphs, goes over the fundamental physics of sound, teaches how it relates to music and harmony, and demonstrates how to build complex tones from simple ones.

This guide is aimed at a general audience–no prior knowledge is required.
[**Check it out!**](https://waveforms.surge.sh/)

* * *

### Future plans

I'm toying with the idea of making this a series. There are other interesting audio concepts to explore. Off the top of my head:

- FFT
- Human perception of sound
- Phase offset effects like phasers, flangers, delays, and reverb
- Distortion (clip distortion, bit reduction)
- FM/AM synthesis
- Envelope generators and filters.

It's likely I won't get to this anytime soon, but do let me know if you think there's a need for interactive explanations of these concepts!

### How It's Made

This tutorial-thingy is purely front-end, built with React. No state management library was needed. Styled with `styled-components`.

The waveforms are rendered with SVG (although they can also render to Canvas with the change of a prop), and the air molecule grids render to Canvas. I used the fancy new IntersectionObserver to handle the scroll-based logic, with a fallback to a simple scroll listener.

> NOTE: This was a very interesting project from a technical perspective! I needed to draw Waveforms in lots of different configurations and states. Waveforms can be one of a series of predefined shapes, or arbitrary shapes (as is the case when converging multiple waveforms together). Waveforms can be "playing", and any state change that can happen (even changing the waveform shape) needs to work whether it's staying still or playing. Also, every transition should use spring physics. Also, it should be performant while doing all of this.

> I started writing up how it works, but I realized that it is super non-trivial, and it deserves a proper blog post. I would like to write that blog post at some point. If this interests you, feel free to > [> poke me on Twitter](https://twitter.com/JoshWComeau)>  and remind me.

> You can also poke around yourself! Check out all the components that start with `Waveform`> , like `WaveformPlayer`>  or `WaveformTween`> .

### Running locally

Want to run this on your machine? it *should* be as simple as `git clone`, `yarn install`, and `yarn:start`. Let me know if that fails.

### Contributing

Please open issues describing changes you'd like to contribute before spending any time working on them; this is a personal side-project, and I open-sourced it primarily as an educational thing, for those curious how it was built. I'm not actively seeking external contributions, and there would be a bit of friction (this repo is no longer the "source of truth" for the project, as it lives on The Pudding).